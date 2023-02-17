from fastapi.testclient import TestClient

from ..testing_utils import world


def test_get_saves_without_auth(client: TestClient) -> None:
    response = client.get("/saves")
    assert response.status_code == 401


def test_get_user_saves(client: TestClient) -> None:
    response = client.get("/saves")
    assert response.json() == [world.save_factory(id=1, user_id=1)]
