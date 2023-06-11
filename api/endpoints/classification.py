from fastapi import APIRouter
from api.model.classify import work_classification, tag_classification
from schemas.user import UserInfo

router = APIRouter()


@router.post('/zero')
async def get_work_scores(temp: UserInfo):
    id = temp.id
    ids = temp.ids
    work_scores = await work_classification(id, ids)
    return work_scores


@router.get('/tag/{id}')
async def get_tag_scores(id):
    tag_scores = await tag_classification(id)
    return tag_scores
