from api.model.similar import get_all_similar
from fastapi import APIRouter

router = APIRouter()


@router.get('/similar/{id}')
async def get_similar(id):
    similar_score = await get_all_similar(id)
    return similar_score
