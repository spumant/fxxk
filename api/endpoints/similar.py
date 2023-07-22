from api.model.similar import get_all_similar
from fastapi import APIRouter
from schemas.user import UserInfo
import json

router = APIRouter()


@router.post("/similar")
async def get_similar(temp: UserInfo):
    id = temp.id
    ids = temp.ids
    similar_score = await get_all_similar(id, ids)
    return similar_score
