import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
POST_DATA = {
    "title": "foo",
    "body": "bar",
    "userId": 1,
}


def test_criar_novo_post():
    response = requests.post(
        f"{BASE_URL}/posts",
        json=POST_DATA,
        headers={"Content-type": "application/json; charset=UTF-8"},
        timeout=10,
    )
    data = response.json()

    assert response.status_code == 201
    assert isinstance(data, dict)
    assert isinstance(data["id"], int)
    assert data["title"] == POST_DATA["title"]
    assert data["body"] == POST_DATA["body"]
    assert data["userId"] == POST_DATA["userId"]
    assert set(["id", "title", "body", "userId"]).issubset(data.keys())
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)
    assert isinstance(data["userId"], int)
