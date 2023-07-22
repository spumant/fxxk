from fastapi import APIRouter
from api.model.workexp import get_exp_year

router = APIRouter()


@router.get("/exp/{id}")
async def get_exp(id):
    years = await get_exp_year(id)
    return years
