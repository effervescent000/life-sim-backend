from fastapi.testclient import TestClient

from ..testing_utils import world


def test_get_all_users(client: TestClient):
    response = client.get("/auth/")
    assert response.json() == [
        {"email": "test@email.com", "id": 1, "username": "some person"}
    ]


def test_post_user(client: TestClient):
    response = client.post(
        "/auth/",
        json={
            "email": "another@email.com",
            "username": "idk something dumb",
            "password": "a password",
        },
    )
    assert response.json() == {
        "id": 2,
        "email": "another@email.com",
        "username": "idk something dumb",
    }


def test_login(client: TestClient):
    user = world.user_factory()
    response = client.post("/auth/login/", json=user)
    assert response.json() == {"access_token": user["username"], "token_type": "bearer"}
