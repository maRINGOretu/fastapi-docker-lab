from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_status():
    response = client.get("/health")
    assert response.status_code == 200


def test_health_body():
    response = client.get("/health")
    assert response.json()["status"] == "ok"


def test_unknown_route():
    response = client.get("/definitely-not-existing")
    assert response.status_code == 404
