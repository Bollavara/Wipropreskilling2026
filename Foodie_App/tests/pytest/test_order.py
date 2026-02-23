import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

def test_view_orders_by_user():
    response = requests.get(f"{BASE_URL}/users/1/orders")
    assert response.status_code == 200

def test_view_orders_by_restaurant():
    response = requests.get(f"{BASE_URL}/restaurants/1/orders")
    assert response.status_code == 200
