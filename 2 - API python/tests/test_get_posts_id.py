import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_buscar_post_com_id_1():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert data["id"] == 1

    for field in ["id", "title", "body", "userId"]:
        assert field in data

    assert data["id"] is not None
    assert isinstance(data["title"], str) and data["title"] != ""
    assert isinstance(data["body"], str) and data["body"] != ""
    assert data["userId"] is not None
    assert len(data["body"]) > 0


def test_buscar_post_com_id_inexistente():
    response = requests.get(f"{BASE_URL}/posts/9999", timeout=10)
    data = response.json()

    assert response.status_code == 404
    assert data == {}
