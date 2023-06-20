from motor.motor_asyncio import AsyncIOMotorClient


async def connect_mongo():
    client = AsyncIOMotorClient('127.0.0.1', 27017)
    db = client['fxxk']
    Item = db['Item']
    return Item


async def connect_result():
    client = AsyncIOMotorClient('127.0.0.1', 27017)
    db = client['fxxk']
    Result = db['result']
    return Result
