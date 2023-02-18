from fastapi.testclient import TestClient

from ..testing_utils import world


def test_get_saves_without_auth(client: TestClient) -> None:
    """Should get bounced with a 401."""
    response = client.get("/saves")
    assert response.status_code == 401


def test_get_user_saves(client: TestClient) -> None:
    """Should include results ONLY from authorized user."""
    response = client.get("/saves", headers=world.AUTH_HEADERS_USER_PRIMARY)
    assert response.json() == [{"active": False, "id": 1, "title": "Untitled"}]


def test_post_save(client: TestClient) -> None:
    save_body = [
        {
            k: v
            for (k, v) in world.save_factory(id=1, user_id=1).items()
            if k not in ["id", "user_id"]
        }
    ]
    response = client.post(
        "/saves", headers=world.AUTH_HEADERS_USER_PRIMARY, json=save_body
    )
    assert response.json() == [{"active": False, "id": 11, "title": "Untitled"}]


def test_update_save(client: TestClient) -> None:
    save_body = [
        {
            k: v
            for (k, v) in world.save_factory(id=1, user_id=1).items()
            if k not in ["user_id"]
        }
    ]
    response = client.post(
        f"/saves/{save_body[0]['id']}",
        headers=world.AUTH_HEADERS_USER_PRIMARY,
        json=save_body,
    )
    assert response.json() == [
        {"active": False, "id": save_body[0]["id"], "title": "Untitled"}
    ]
