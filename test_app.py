# test_app.py
from app import app

def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b'Hello, World!'

