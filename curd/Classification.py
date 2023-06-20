from database.mongodb import connect_mongo
import asyncio
import nest_asyncio
from models.base import Job

nest_asyncio.apply()


async def get_all_text(id):
    Item = await connect_mongo()
    id = int(id)
    item = await Item.find_one({'id': {'$eq': id}})
    skill = item['skills']
    skill_str = "个人技能：" + skill
    jobHunt_str = "求职意愿：" + item['jobHunt']
    # experiences_str = "工作经历：" + item['experiences']
    # educational_str = "教育经历" + item['educational']
    self_str = item['self']
    award_str = "获奖证书：" + item['award']
    text = skill_str + jobHunt_str + self_str + award_str
    return text


async def get_work_cla_dict(work_cla):
    labels = work_cla['labels']
    scores = work_cla['scores']

    work_dict = {}

    length = len(labels)
    for i in range(length):
        work_dict[labels[i]] = scores[i]

    return work_dict


async def get_tag_dict(tag_cla):
    labels = tag_cla['labels']
    scores = tag_cla['scores']

    tag_dict = {
        labels[0]: scores[0],
        labels[1]: scores[1]
    }

    return tag_dict


async def get_candidate(ids):
    Infos = await Job.filter(jid__in=ids).values('jname')
    cand = []
    for info in Infos:
        cand.append(info['jname'])
    return cand
