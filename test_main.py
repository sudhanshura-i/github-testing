import pytest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_read_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "name": "Item 42"}


def test_read_item_invalid():
    response = client.get("/items/invalid")
    assert response.status_code == 422


def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Widget", "price": 9.99}
    )
    assert response.status_code == 200
    assert response.json()["created"] is True
    assert response.json()["item"]["name"] == "Widget"
    assert response.json()["item"]["price"] == 9.99


def test_create_item_missing_field():
    response = client.post(
        "/items/",
        json={"name": "Widget"}
    )
    assert response.status_code == 422