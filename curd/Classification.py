from database.mongodb import connect_mongo


async def get_all_text(id):
    Item = connect_mongo()
    item = await Item.find_one({'id': id})
    skill = item['skill']
    skill_str = "个人技能：" + "，".join(skill)
    jobHunt_str = "求职意愿：" + item['jobHunt']
    experiences_str = "工作经历：" + item['experiences']
    educational_str = "教育经历" + item['educational']
    award_str = "获奖证书：" + "，".join(item['award'])
    text = skill_str + jobHunt_str + experiences_str + educational_str + award_str
    return text


async def get_work_cla_dict(work_cla):
    labels = work_cla['labels']
    scores = work_cla['scores']

    work_dict = {
        labels[0]: scores[0],
        labels[1]: scores[1],
        labels[2]: scores[2],
        labels[3]: scores[3],
        labels[4]: scores[4]
    }

    return work_dict


async def get_tag_dict(tag_cla):
    labels = tag_cla['labels']
    scores = tag_cla['scores']

    tag_dict = {
        labels[0]: scores[1],
        labels[1]: scores[1]
    }

    return tag_dict
