import os
import shutil
import tempfile
import pytest
import sqlite3


def create_db(file_name):
    conn = sqlite3.connect(file_name)
    conn.commit()
    conn.close()

from hello_flask import create_app

@pytest.fixture
def client():
    # Set up temporary DB
    temp_path = tempfile.mkdtemp()
    temp_file = temp_path + "/test.db"
    create_db(temp_file)
    URI = "sqlite:///%s" % temp_file

    app = create_app(URI)
    client = app.test_client()

    yield client

    shutil.rmtree(temp_path)