import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_movies():
    response = requests.get(f"{BASE_URL}/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_movie():
    payload = {
        "id": 102,
        "movie_name": "Inception",
        "language": "English",
        "duration": "2h 28m",
        "price": 220
    }
    response = requests.post(f"{BASE_URL}/api/movies", json=payload)
    assert response.status_code == 201

def test_book_ticket():
    payload = {
        "movie_id": 101,
        "seats": 2
    }
    response = requests.post(f"{BASE_URL}/api/bookings", json=payload)
    assert response.status_code == 201
