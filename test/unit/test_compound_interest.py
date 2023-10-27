from app.services.compound_interest_service import calculate_compound_interest
from app.schemas.compound_interest import CompoundInterestInput


def test_calculate_compound_interest():
    data = CompoundInterestInput(principal=1000, rate=5, time=10, frequency=12)
    result = calculate_compound_interest(data)
    assert result.total_amount > 1000
    assert result.interest_amount > 0
