import json


def test_classes_get(client):
    response = client.get('/api/v1/status')
    json_data = json.loads(response.data)
    print(json_data)