from fastapi import APIRouter
from api.model.classify import work_classification, tag_classification
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get('/zero/{id}')
async def get_work_scores(id):
    work_scores = await work_classification(id)
    return work_scores


@router.get('/tag/{id}')
async def get_tag_scores(id):
    tag_scores = await tag_classification(id)
    return tag_scores
