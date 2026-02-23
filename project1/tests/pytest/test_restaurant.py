import requests

BASE_URL = "http://localhost:5000/api/v1"


def test_register_restaurant():
    payload = {
        "name": "Food Hub",
        "category": "Indian",
        "location": "Hyderabad",
        "images": [],
        "contact": "9876543210"
    }

    response = requests.post(f"{BASE_URL}/restaurants", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Food Hub"


def test_get_restaurant():
    response = requests.get(f"{BASE_URL}/restaurants/1")
    assert response.status_code == 200


def test_update_restaurant():
    payload = {"location": "Bangalore"}
    response = requests.put(f"{BASE_URL}/restaurants/1", json=payload)
    assert response.status_code == 200
    assert response.json()["location"] == "Bangalore"


def test_disable_restaurant():
    response = requests.put(f"{BASE_URL}/restaurants/1/disable")
    assert response.status_code == 200
