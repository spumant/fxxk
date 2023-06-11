import torch

from api.endpoints.classification import get_work_scores, get_tag_scores
from api.endpoints.similar import get_similar
import torch.nn.functional as F
from fastapi import APIRouter
from schemas.user import UserInfo
from curd.Classification import get_candidate

router = APIRouter()


@router.post('/all')
async def get_all(temp: UserInfo):
    id = temp.id
    ids = temp.ids
    work_scores = await get_work_scores(temp)
    similar_scores = await get_similar(temp)
    tag_scores = await get_tag_scores(id)
    cands = await get_candidate(ids)

    all_scores = []

    for cand in cands:
        scores = {cand: work_scores[cand] + similar_scores[cand]}
        all_scores.append(scores)

    before = []
    for score in all_scores:
        before.append(list(score.values())[0])

    print(before)

    final = F.softmax(torch.tensor(before))
    all_scores_final = []
    for i in range(len(all_scores)):
        tmp = {list(all_scores[i].keys())[0]: final[i].item()}
        all_scores_final.append(tmp)
    if tag_scores['工作变动稳定'] > tag_scores['工作变动频繁']:
        all_scores_final.append({"tag": '工作变动稳定'})
    elif tag_scores['工作变动稳定'] < tag_scores['工作变动频繁']:
        all_scores_final.append({"tag": '工作变动频繁'})

    all_dict = {}
    for dic in all_scores_final:
        all_dict = {**all_dict, **dic}

    return all_dict
