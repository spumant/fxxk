import random

from schemas.user import UserInfo, SortInfo
from fastapi import APIRouter
from curd.all import get_all_dict, to_mongodb
from database.mongodb import connect_result
from curd.mysort import mine
from test import test
from api.endpoints.classification import get_tag_scores

router = APIRouter()


@router.post("/all")
async def get_all(temp: UserInfo):
    all_dict = await get_all_dict(temp)
    await to_mongodb(all_dict)
    return all_dict


@router.get("/all/{id}")
async def get_result(id):
    id = int(id)
    result = await connect_result()
    document = await result.find_one({"id": id}, {"_id": 0})
    return document


@router.post("/sort")
async def get_sorted(temp: SortInfo):
    ids = temp.ids
    condition = temp.condition
    return await mine(ids, condition)


@router.get("/degree/{id}")
async def tag(id):
    id = int(id)
    document = await get_result(id)
    if document["tag"] == "工作变动频繁":
        return random.randint(80, 100)
    else:
        return random.randint(1, 20)


@router.get("/test")
async def start():
    await test()
