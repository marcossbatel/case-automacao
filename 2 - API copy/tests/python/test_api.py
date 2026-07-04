import json
import urllib.error
import urllib.request

import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


def _request(method, path, payload=None, headers=None):
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        f"{BASE_URL}{path}",
        data=data,
        method=method,
        headers=headers or {},
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            body = response.read().decode("utf-8")
            return response.status, json.loads(body)
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8")
        return error.code, json.loads(body)


def test_get_posts_by_user():
    status, payload = _request("GET", "/posts?userId=1")

    assert status == 200
    assert isinstance(payload, list)
    assert payload, "A lista de posts não pode estar vazia"
    assert all(item["userId"] == 1 for item in payload)
    assert all({"id", "title", "body", "userId"}.issubset(item.keys()) for item in payload)


def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }

    status, response_body = _request(
        "POST",
        "/posts",
        payload=payload,
        headers={"Content-Type": "application/json; charset=UTF-8"},
    )

    assert status == 201
    assert isinstance(response_body, dict)
    assert response_body["title"] == "foo"
    assert response_body["body"] == "bar"
    assert response_body["userId"] == 1
    assert response_body["id"] is not None


def test_get_post_by_id():
    status, payload = _request("GET", "/posts/1")

    assert status == 200
    assert isinstance(payload, dict)
    assert payload["id"] == 1
    assert payload["userId"] == 1
    assert {"id", "title", "body", "userId"}.issubset(payload.keys())


def test_get_posts_for_user_without_posts():
    status, payload = _request("GET", "/posts?userId=999")

    assert status == 200
    assert payload == []


def test_get_post_by_id_not_found():
    status, payload = _request("GET", "/posts/999")

    assert status == 404
    assert payload == {}
