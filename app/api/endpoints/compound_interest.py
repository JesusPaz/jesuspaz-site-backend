from fastapi import APIRouter
from app.schemas.compound_interest import CompoundInterestInput, CompoundInterestYearDetail
from app.services import compound_interest_service
from typing import List

router = APIRouter()


@router.post("/compound-interest/", response_model=List[CompoundInterestYearDetail])
async def calculate_compound_interest(
    data: CompoundInterestInput
) -> List[CompoundInterestYearDetail]:

    """
    Calculate compound interest based on provided input.
    """
    result = compound_interest_service.calculate_compound_interest_details(
        data)
    return result
