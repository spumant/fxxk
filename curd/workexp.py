from database.mongodb import connect_mongo
from schemas.resume import ItemCheck


async def get_context(id: str):
    Item = connect_mongo()
    item = await Item.find_one({'id': id})
    return item['experiences']
