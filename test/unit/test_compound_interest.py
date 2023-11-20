from app.services.compound_interest_service import calculate_compound_interest_details
from app.schemas.compound_interest import CompoundInterestInput


def test_calculate_compound_interest():
    data = CompoundInterestInput(principal=1000, rate=5, time=10, frequency=12, contribution=100, contribution_frequency=12)
    results = calculate_compound_interest_details(data)

    # Ensure that a result is returned for each year
    assert len(results) == data.time

    # Check that each year has a final balance greater than the initial balance
    for detail in results:
        assert detail.Final_Balance > detail.Initial_Balance

    # Verify that the total interest and contributions are positive
    total_interest = sum([detail.Yearly_Interest for detail in results])
    total_contributions = sum([detail.Yearly_Contributions for detail in results])
    assert total_interest > 0
    assert total_contributions == data.contribution * data.contribution_frequency * data.time
