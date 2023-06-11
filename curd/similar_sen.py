from models.base import Job


async def get_information(ids):
    Info = await Job.filter(jid__in=ids).values('jname', 'jneed_other')
    return Info
