import requests

database = {
    1: "Alice",
    2: "Bobby",
    3: "Charles"
}


def get_user_from_db(user_id):
    return database.get(user_id)


def get_users():
    response = requests.get("https://jsonplaceholders.typicode.com/users")
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError
