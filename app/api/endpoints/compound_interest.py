from fastapi import APIRouter, Depends, HTTPException
from app.schemas.compound_interest import CompoundInterestInput, CompoundInterestOutput
from app.services import compound_interest_service

router = APIRouter()


@router.post("/compound-interest/", response_model=CompoundInterestOutput)
async def calculate_compound_interest(
    data: CompoundInterestInput
) -> CompoundInterestOutput:
    """
    Calculate compound interest based on provided input.
    """
    result = compound_interest_service.calculate(data)
    return result
