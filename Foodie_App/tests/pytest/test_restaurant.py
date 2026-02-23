import requests
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"

def create_restaurant():
    payload = {
        "name": f"Res_{uuid.uuid4()}",
        "category": "Indian",
        "location": "Hyderabad",
        "images": [],
        "contact": "9999999999"
    }
    return requests.post(f"{BASE_URL}/restaurants", json=payload)

def test_register_restaurant():
    response = create_restaurant()
    assert response.status_code == 201

def test_update_restaurant():
    res = create_restaurant()
    rid = res.json()["id"]

    response = requests.put(
        f"{BASE_URL}/restaurants/{rid}",
        json={"location": "Chennai"}
    )
    assert response.status_code == 200

def test_disable_restaurant():
    res = create_restaurant()
    rid = res.json()["id"]

    response = requests.put(f"{BASE_URL}/restaurants/{rid}/disable")
    assert response.status_code == 200

def test_view_restaurant_profile():
    res = create_restaurant()
    rid = res.json()["id"]

    response = requests.get(f"{BASE_URL}/restaurants/{rid}")
    assert response.status_code == 200
