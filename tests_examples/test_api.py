import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_get_posts():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_post():
    post_id = 1
    response = requests.get(f"{BASE_URL}/{post_id}")

    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["id"] == post_id

def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    data = response.json()
    print(data)
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]

def test_update_post():
    post_id = 1
    updated_data = {
        "id": post_id,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/{post_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["title"] == updated_data["title"]

def test_delete_post():
    post_id = 1
    response = requests.delete(f"{BASE_URL}/{post_id}")
    assert response.status_code == 200
