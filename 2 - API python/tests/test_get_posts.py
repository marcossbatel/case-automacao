import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_listar_todos_os_posts():
    response = requests.get(f"{BASE_URL}/posts", timeout=10)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    for post in data:
        assert "userId" in post
        assert "id" in post
        assert "title" in post
        assert "body" in post
        assert post["userId"] is not None
        assert post["id"] is not None
        assert isinstance(post["title"], str) and post["title"] != ""
        assert isinstance(post["body"], str) and post["body"] != ""
