from pydantic import BaseModel, Field


class CompoundInterestInput(BaseModel):
    principal: float = Field(...,
                             description="The initial amount of money that was deposited or loaned.",
                             gt=0)
    rate: float = Field(...,
                        description="The annual interest rate (as a percentage). For example, 10 signifies 10%.",
                        gt=0, lt=100)
    time: float = Field(...,
                        description="The number of years the money is invested or borrowed for.",
                        gt=0)
    frequency: int = Field(...,
                           description="The number of times interest is applied per time period.",
                           gt=0)


class CompoundInterestOutput(BaseModel):
    total_amount: float = Field(...,
                                description="The total amount after the time period, which includes the principal amount plus the compounded interest.")
    interest_amount: float = Field(...,
                                   description="The total amount of interest earned or paid over the time period.")
