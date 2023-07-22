from curd.all import get_all_dict
from models.base import Worker
from schemas.user import UserInfo
from collections import OrderedDict
import json


# userinfo = {
#     "id": "",
#     "ids": list(range(10))
# }
async def test():
    result = OrderedDict()
    for i in range(1, 301):
        worker = await Worker.filter(wid=i).values('worker_name', 'age', 'edu_level', 'edu_school', 'work_year')
        userinfo = UserInfo(id=i, ids=list(range(1, 11)))
        job = await get_all_dict(userinfo)
        job['id'] = 0
        match = max(job, key=job.get)
        print(match)
        result[str(i)] = {
            "name": worker[0]['worker_name'],
            "age": worker[0]['age'],
            "education": worker[0]['edu_level'],
            "school": worker[0]['edu_school'],
            "work_time": worker[0]['work_year'],
            "match_position": match
        }

    json_str = json.dumps(result, indent=4, ensure_ascii=False)
    with open('test_data.json', 'w') as json_file:
        json_file.write(json_str)
