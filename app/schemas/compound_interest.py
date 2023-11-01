from pydantic import BaseModel, Field
from typing import List


class CompoundInterestInput(BaseModel):
    principal: float = Field(...,
                             description="The initial amount of money that was deposited or loaned.",
                             gt=0)
    rate: float = Field(...,
                        description="The annual interest rate (as a percentage). For example, 10 signifies 10%.",
                        gt=0, lt=1000)
    time: float = Field(...,
                        description="The number of years the money is invested or borrowed for.",
                        gt=0)
    frequency: int = Field(...,
                           description="The number of times interest is applied per time period.",
                           gt=0)
    contribution: float = 0
    contribution_frequency: int = 12


class CompoundInterestYearDetail(BaseModel):
    Year: int = Field(..., description="The year number.")
    Initial_Balance: float = Field(...,
                                   description="The balance at the start of the year.")
    Yearly_Contributions: float = Field(
        ..., description="The total contributions made during the year.")
    Total_Contributions: float = Field(
        ..., description="The cumulative contributions up to this year.")
    Yearly_Interest: float = Field(...,
                                   description="The interest earned or paid during the year.")
    Total_Interest: float = Field(...,
                                  description="The cumulative interest up to this year.")
    Final_Balance: float = Field(
        ..., description="The balance at the end of the year after adding contributions and interest.")


class CompoundInterestOutput(List[CompoundInterestYearDetail]):
    pass
