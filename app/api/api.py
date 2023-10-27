from fastapi import APIRouter

from app.api.endpoints import compound_interest

router = APIRouter()

router.include_router(compound_interest.router, tags=[
                      "Compound Interest"], prefix="/finance")
