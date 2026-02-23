import requests
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"


def test_add_dish():
    # Step 1: Create Restaurant first
    restaurant_payload = {
        "name": f"Res_{uuid.uuid4()}",
        "category": "Indian",
        "location": "Hyderabad",
        "images": [],
        "contact": "9999999999"
    }

    restaurant_response = requests.post(
        f"{BASE_URL}/restaurants", json=restaurant_payload
    )

    restaurant_id = restaurant_response.json()["id"]

    # Step 2: Add Dish to that restaurant
    dish_payload = {
        "name": "Biryani",
        "type": "Non-Veg",
        "price": 250,
        "available_time": "Lunch",
        "image": ""
    }

    response = requests.post(
        f"{BASE_URL}/restaurants/{restaurant_id}/dishes",
        json=dish_payload
    )

    assert response.status_code == 201


def test_update_dish():
    # Step 1: Create restaurant
    r = requests.post(f"{BASE_URL}/restaurants", json={
        "name": "TestRes",
        "category": "Indian",
        "location": "Hyd",
        "images": [],
        "contact": "123"
    })

    restaurant_id = r.json()["id"]

    # Step 2: Create dish
    d = requests.post(f"{BASE_URL}/restaurants/{restaurant_id}/dishes", json={
        "name": "Biryani",
        "type": "Veg",
        "price": 250,
        "available_time": "Lunch",
        "image": "img.jpg"
    })

    dish_id = d.json()["id"]

    # Step 3: Update dish
    response = requests.put(f"{BASE_URL}/dishes/{dish_id}", json={"price": 300})

    assert response.status_code == 200


#def test_enable_disable_dish():
#    payload = {"enabled": False}
#    response = requests.put(f"{BASE_URL}/dishes/1/status", json=payload)
#    assert response.status_code == 200
def test_enable_disable_dish():
    # Step 1: Create restaurant
    restaurant_payload = {
        "name": f"Res_Test",
        "category": "Indian",
        "location": "Hyderabad",
        "images": [],
        "contact": "9999999999"
    }

    restaurant_response = requests.post(
        f"{BASE_URL}/restaurants",
        json=restaurant_payload
    )

    restaurant_id = restaurant_response.json()["id"]

    # Step 2: Add dish
    dish_payload = {
        "name": "Biryani",
        "type": "Non-Veg",
        "price": 250,
        "available_time": "Lunch",
        "image": ""
    }

    dish_response = requests.post(
        f"{BASE_URL}/restaurants/{restaurant_id}/dishes",
        json=dish_payload
    )

    dish_id = dish_response.json()["id"]

    # Step 3: Disable dish
    response = requests.put(
        f"{BASE_URL}/dishes/{dish_id}/status",
        json={"enabled": False}
    )

    assert response.status_code == 200


#def test_delete_dish():
#    response = requests.delete(f"{BASE_URL}/dishes/1")
#    assert response.status_code == 200
def test_delete_dish():
    # Step 1: Create restaurant
    restaurant_payload = {
        "name": f"Res_Delete",
        "category": "Indian",
        "location": "Hyderabad",
        "images": [],
        "contact": "9999999999"
    }

    restaurant_response = requests.post(
        f"{BASE_URL}/restaurants",
        json=restaurant_payload
    )

    restaurant_id = restaurant_response.json()["id"]

    # Step 2: Add dish
    dish_payload = {
        "name": "Paneer",
        "type": "Veg",
        "price": 200,
        "available_time": "Dinner",
        "image": ""
    }

    dish_response = requests.post(
        f"{BASE_URL}/restaurants/{restaurant_id}/dishes",
        json=dish_payload
    )

    dish_id = dish_response.json()["id"]

    # Step 3: Delete dish
    response = requests.delete(
        f"{BASE_URL}/dishes/{dish_id}"
    )

    assert response.status_code == 200
