import requests
import uuid

BASE_URL = "http://localhost:5000/api/v1"


def test_user_registration():
    unique_email = f"user_{uuid.uuid4()}@gmail.com"

    payload = {
        "name": "TestUser",
        "email": unique_email,
        "password": "12345"
    }

    response = requests.post(f"{BASE_URL}/users/register", json=payload)

    assert response.status_code == 201


def test_place_order():
    payload = {
        "user_id": 1,
        "restaurant_id": 1,
        "dishes": [1]
    }

    response = requests.post(f"{BASE_URL}/orders", json=payload)
    assert response.status_code == 201


def test_view_orders_by_user():
    response = requests.get(f"{BASE_URL}/users/1/orders")
    assert response.status_code == 200


def test_view_orders_by_restaurant():
    response = requests.get(f"{BASE_URL}/restaurants/1/orders")
    assert response.status_code == 200
