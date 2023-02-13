from fastapi.testclient import TestClient


def test_get_all_users(client: TestClient):
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == [
        {"email": "test@email.com", "id": 1, "name": "some person"}
    ]


def test_post_user(client: TestClient):
    response = client.post(
        "/users/new",
        json={
            "email": "another@email.com",
            "name": "idk something dumb",
            "hashed_password": "a password",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "email": "another@email.com",
        "name": "idk something dumb",
    }
