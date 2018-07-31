import os
import shutil
import tempfile
import pytest
import sqlite3

from hello_flask import app

def create_db(file_name):
    conn = sqlite3.connect(file_name)
    conn.commit()
    conn.close()

@pytest.fixture
def client():
    temp_path = tempfile.mkdtemp()
    temp_file = temp_path + "/test.db"
    create_db(temp_file)
    print("sqlite:///%s" % temp_file)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///%s" % temp_file
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

    shutil.rmtree(temp_path)