from app.schemas.compound_interest import CompoundInterestInput, CompoundInterestOutput


def calculate_compound_interest(data: CompoundInterestInput) -> CompoundInterestOutput:
    """
    Calculate the compound interest based on the given data.

    Parameters:
    - data (CompoundInterestInput): The input data including principal, rate, time, and frequency.

    Returns:
    - CompoundInterestOutput: The calculated total amount and interest amount.
    """
    # Extract the data
    principal = data.principal
    rate = data.rate / 100  # Convert the rate from percentage to a fraction
    time = data.time
    frequency = data.frequency

    # Compound interest formula: A = P(1 + r/n)^(nt)
    total_amount = principal * (1 + rate / frequency) ** (frequency * time)

    # Calculate the interest earned
    interest_amount = total_amount - principal

    return CompoundInterestOutput(total_amount=total_amount, interest_amount=interest_amount)
