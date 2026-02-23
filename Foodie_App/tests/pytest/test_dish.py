import requests
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"

def setup_restaurant():
    payload = {
        "name": f"DishRes_{uuid.uuid4()}",
        "category": "Indian",
        "location": "Hyd",
        "images": [],
        "contact": "9999999999"
    }
    return requests.post(f"{BASE_URL}/restaurants", json=payload)

def test_add_dish():
    res = setup_restaurant()
    rid = res.json()["id"]

    payload = {
        "name": "Biryani",
        "type": "Non-Veg",
        "price": 250,
        "available_time": "Lunch",
        "image": ""
    }

    response = requests.post(f"{BASE_URL}/restaurants/{rid}/dishes", json=payload)
    assert response.status_code == 201

def test_update_dish():
    res = setup_restaurant()
    rid = res.json()["id"]

    dish = requests.post(
        f"{BASE_URL}/restaurants/{rid}/dishes",
        json={"name": "Fried Rice", "type": "Veg", "price": 150, "available_time": "Lunch", "image": ""}
    )
    did = dish.json()["id"]

    response = requests.put(f"{BASE_URL}/dishes/{did}", json={"price": 200})
    assert response.status_code == 200

def test_enable_disable_dish():
    res = setup_restaurant()
    rid = res.json()["id"]

    dish = requests.post(
        f"{BASE_URL}/restaurants/{rid}/dishes",
        json={"name": "Noodles", "type": "Veg", "price": 120, "available_time": "Dinner", "image": ""}
    )
    did = dish.json()["id"]

    response = requests.put(f"{BASE_URL}/dishes/{did}/status", json={"enabled": False})
    assert response.status_code == 200

def test_delete_dish():
    res = setup_restaurant()
    rid = res.json()["id"]

    dish = requests.post(
        f"{BASE_URL}/restaurants/{rid}/dishes",
        json={"name": "Pizza", "type": "Veg", "price": 300, "available_time": "Dinner", "image": ""}
    )
    did = dish.json()["id"]

    response = requests.delete(f"{BASE_URL}/dishes/{did}")
    assert response.status_code == 200
