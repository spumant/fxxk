import torch

from api.endpoints.classification import get_work_scores, get_tag_scores
from api.endpoints.similar import get_similar
import torch.nn.functional as F
from schemas.user import UserInfo
from curd.Classification import get_candidate
from database.mongodb import connect_result


async def get_all_dict(temp: UserInfo):
    id = temp.id
    ids = temp.ids
    # 整合所有模型
    work_scores = await get_work_scores(temp)
    similar_scores = await get_similar(temp)
    tag_scores = await get_tag_scores(id)
    cands = await get_candidate(ids)

    all_scores = []
    # 将相似度模型的结果与分类模型的结果求和
    for cand in cands:
        scores = {cand: work_scores[cand] + similar_scores[cand]}
        all_scores.append(scores)
    # 重新分类之前的处理
    before = []
    for score in all_scores:
        before.append(list(score.values())[0])

    print(before)
    # 重新分类
    final = F.softmax(torch.tensor(before))

    # 信息整合到一个字典里
    all_scores_final = [{'id': id}]

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


async def to_mongodb(all_dict):
    result = await connect_result()
    result.insert_one(all_dict)