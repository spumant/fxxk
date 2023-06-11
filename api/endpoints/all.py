from api.endpoints.classification import get_work_scores, get_tag_scores
from api.endpoints.similar import get_all_similar
import torch.nn as nn
from fastapi import APIRouter

router = APIRouter()


@router.get('/all/{id}')
async def get_all(id):
    work_scores = get_work_scores(id)
    similar_scores = get_all_similar(id)

    all_scores = {

    }
