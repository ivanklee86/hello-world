import json


SAMPLE_INSERT = {
    "comment": "my comment",
    "description": "lalala"
}

UPDATE_INSERT = {
    "comment": "my comment2",
    "description": "lalala"
}

def test_status_GET(client):
    response = client.get('/api/v1/status')
    json_data = json.loads(response.data)
    assert json_data == "OK"

def test_entries_GET(client):
    response = client.get('/api/v1/entries')
    json_data = json.loads(response.data)
    assert len(json_data) == 0

def test_entries_POST(client):
    response = client.post('/api/v1/entries',
                           data=json.dumps(SAMPLE_INSERT),
                           content_type="application/json")
    json_data = json.loads(response.data)
    assert json_data['comment'] == SAMPLE_INSERT['comment']
    assert json_data['id'] == 1

def test_entries_id_GET(client):
    client.post('/api/v1/entries',
               data=json.dumps(SAMPLE_INSERT),
               content_type="application/json")

    response = client.get('/api/v1/entries/1')
    json_data = json.loads(response.data)
    assert json_data['comment'] == SAMPLE_INSERT['comment']
    assert json_data['id'] == 1

def test_entries_id_POST(client):
    client.post('/api/v1/entries',
               data=json.dumps(SAMPLE_INSERT),
               content_type="application/json")

    response = client.post('/api/v1/entries/1',
                           data=json.dumps(UPDATE_INSERT),
                           content_type="application/json")

    json_data = json.loads(response.data)
    assert json_data['comment'] == UPDATE_INSERT['comment']

def test_entries_id_DELETE(client):
    client.post('/api/v1/entries',
               data=json.dumps(SAMPLE_INSERT),
               content_type="application/json")

    response = client.delete('/api/v1/entries/1')
    assert response.status_code == 204