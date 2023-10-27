from app.schemas.compound_interest import CompoundInterestInput, CompoundInterestOutput, CompoundInterestYearDetail


def calculate_compound_interest_details(data: CompoundInterestInput) -> CompoundInterestOutput:
    principal = data.principal
    rate = data.rate / 100
    time = int(data.time)
    frequency = data.frequency
    contribution = data.contribution * \
        data.contribution_frequency  # total contribution per year

    results = []

    for year in range(1, time + 1):
        # Compound interest for the principal
        principal = principal * (1 + rate/frequency)**frequency

        # Future value of the contributions for this year
        contributions_fv = contribution * \
            ((1 + rate/frequency)**frequency - 1) * (frequency/rate)

        # Update principal with the contributions
        principal += contributions_fv

        # Append the details for this year to the results
        results.append(CompoundInterestYearDetail(
            Year=year,
            # remove this year contributions for initial balance
            Initial_Balance=principal - contributions_fv,
            Yearly_Contributions=contribution,
            Total_Contributions=contribution * year,  # total contributions until this year
            # total - initial balance - this year contribution
            Yearly_Interest=principal - \
            (principal - contributions_fv) - contribution,
            Total_Interest=principal - data.principal - contribution * \
            year,  # total - initial principal - total contributions
            Final_Balance=principal
        ))

    return results
