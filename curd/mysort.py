from database.mongodb import connect_result
from models.base import Worker

edu = {
    "博士": 0,
    "硕士": 1,
    "本科": 2,
    "大专": 3,
    "中专": 4
}


async def workinfo(ids):
    info = await Worker.filter(wid__in=ids).values('wid', 'edu_level', 'work_year')
    return info


async def screen(ids, condition):
    info = await workinfo(ids)
    for item in info:
        item['wid'] = int(item['wid'])
        item['edu_level'] = edu[item['edu_level']]
        item['work_year'] = int(item['work_year'])
        if item['work_year'] < condition['work_year']:
            info.remove(item)
        # for item in info:
        if item['edu_level'] > condition['edu_level']:
            info.remove(item)

    return info


async def mine(ids, condition):
    condition['edu_level'] = int(condition['edu_level'])
    condition['work_year'] = int(condition['work_year'])
    job = condition['job']
    info = await screen(ids, condition)
    result = await connect_result()
    for item in info:
        id = item['wid']
        document = await result.find_one({'id': int(id)}, {'_id': 0})
        # print(document)
        item.update(document)
    print(info)
    sorted(info, key=lambda d: d[job], reverse=True)
    wids = []
    for item in info:
        wids.append(item['wid'])
    return wids
