from schemas.user import UserInfo
from fastapi import APIRouter
from curd.all import get_all_dict, to_mongodb
from database.mongodb import connect_result

router = APIRouter()


@router.post('/all')
async def get_all(temp: UserInfo):
    all_dict = await get_all_dict(temp)
    await to_mongodb(all_dict)
    return all_dict


@router.get('/all/{id}')
async def get_result(id):
    id = int(id)
    result = await connect_result()
    document = await result.find_one({'id': id}, {'_id': 0})
    return document
