from fastapi.testclient import TestClient
from app.server import app

client = TestClient(app)


def test_compound_interest_endpoint():
    response = client.post(
        "/finance/compound-interest/", json={"principal": 1000, "rate": 5, "time": 10, "frequency": 12})
    assert response.status_code == 200
    data = response.json()
    assert "total_amount" in data
    assert "interest_amount" in data
