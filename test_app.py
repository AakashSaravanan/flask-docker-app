from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_response_contains_hello():
    client = app.test_client()
    response = client.get('/')
    assert b'Hello' in response.data
