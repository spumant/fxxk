from database.mongodb import connect_mongo
from schemas.resume import ItemCheck


async def get_context(id: str):
    Item = await connect_mongo()
    id = int(id)
    item = await Item.find_one({'id': id})
    return item['self']
