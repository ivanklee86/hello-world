import shutil
import tempfile
import pytest
import sqlite3
from hello_flask import create_app

def create_db(file_name):
    # Creates a temporary sqlite database
    conn = sqlite3.connect(file_name)
    conn.commit()
    conn.close()

@pytest.fixture
def client():
    # Sets up a temporary database.
    temp_path = tempfile.mkdtemp()
    temp_file = temp_path + "/test.db"
    create_db(temp_file)
    URI = "sqlite:///%s" % temp_file

    # Yields a test client.
    app = create_app(URI)
    client = app.test_client()
    yield client

    #Cleans up temporary db.
    shutil.rmtree(temp_path)