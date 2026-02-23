import requests
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"

def create_restaurant():
    return requests.post(f"{BASE_URL}/restaurants", json={
        "name": f"AdminRes_{uuid.uuid4()}",
        "category": "Indian",
        "location": "Hyd",
        "images": [],
        "contact": "9999999999"
    })

def test_admin_approve_restaurant():
    res = create_restaurant()
    rid = res.json()["id"]

    response = requests.put(f"{BASE_URL}/admin/restaurants/{rid}/approve")
    assert response.status_code == 200

def test_admin_disable_restaurant():
    res = create_restaurant()
    rid = res.json()["id"]

    response = requests.put(f"{BASE_URL}/admin/restaurants/{rid}/disable")
    assert response.status_code == 200

def test_view_feedback():
    response = requests.get(f"{BASE_URL}/admin/feedback")
    assert response.status_code == 200

def test_view_order_status():
    response = requests.get(f"{BASE_URL}/admin/orders")
    assert response.status_code == 200
