import pytest
import requests

@pytest.mark.parametrize("payload", [
    {"name": "Harika", "age": 22, "gender": "Female", "contact": "9876543210", "disease": "Fever", "doctor": "Dr. Smith"},
    {"name": "Krupa", "age": 23, "gender": "Male", "contact": "9876501234", "disease": "Cold", "doctor": "Dr. Jones"}
])
def test_add_patient(base_url, payload):
    response = requests.post(f"{base_url}/patients", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == payload['name']

def test_get_patients(base_url):
    response = requests.get(f"{base_url}/patients")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_invalid_patient(base_url):
    response = requests.post(f"{base_url}/patients", json={"age": 25})
    assert response.status_code == 400
