from fastapi.testclient import TestClient
from app.server import app

client = TestClient(app)


def test_compound_interest_endpoint():
    response = client.post(
        "/finance/compound-interest/",
        json={"principal": 1000, "rate": 5, "time": 10, "frequency": 12}
    )
    assert response.status_code == 200
    data = response.json()

    # Assuming the final balance is the 'total_amount'
    final_balance = data[-1]['Final_Balance']
    assert final_balance > 1000  # Final balance should be greater than the principal

    # Assuming you want to check if there's a positive interest amount
    total_interest = sum([year_detail['Yearly_Interest'] for year_detail in data])
    assert total_interest > 0  # Total interest should be positive
