import requests
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"

def test_user_registration():
    payload = {
        "name": "TestUser",
        "email": f"user_{uuid.uuid4()}@gmail.com",
        "password": "12345"
    }

    response = requests.post(f"{BASE_URL}/users/register", json=payload)
    assert response.status_code == 201

def test_search_restaurants():
    response = requests.get(f"{BASE_URL}/restaurants/search?location=Hyderabad")
    assert response.status_code == 200

def test_place_order():
    # create user
    user = requests.post(f"{BASE_URL}/users/register", json={
        "name": "OrderUser",
        "email": f"order_{uuid.uuid4()}@gmail.com",
        "password": "12345"
    })
    uid = user.json()["id"]

    # create restaurant
    res = requests.post(f"{BASE_URL}/restaurants", json={
        "name": f"OrderRes_{uuid.uuid4()}",
        "category": "Indian",
        "location": "Hyd",
        "images": [],
        "contact": "9999999999"
    })
    rid = res.json()["id"]

    # add dish
    dish = requests.post(
        f"{BASE_URL}/restaurants/{rid}/dishes",
        json={"name": "Burger", "type": "Veg", "price": 100, "available_time": "Lunch", "image": ""}
    )
    did = dish.json()["id"]

    # place order
    response = requests.post(
        f"{BASE_URL}/orders",
        json={"user_id": uid, "restaurant_id": rid, "dishes": [did]}
    )

    assert response.status_code == 201

def test_give_rating():
    response = requests.post(
        f"{BASE_URL}/ratings",
        json={"order_id": 1, "rating": 5, "comment": "Excellent"}
    )
    # Depending on your logic
    assert response.status_code in [201, 400]
