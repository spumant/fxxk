from curd.Classification import get_all_text
from curd.similar_sen import Clerks_score, Marketing_score, Product_score, Finance_score, Project_score


async def get_all_similar(id):
    sentence = await get_all_text(id)
    # print("*************************************************************")
    # print(sentence)
    Cscore = await Clerks_score(sentence)
    Mscore = await Marketing_score(sentence)
    Pscore = await Product_score(sentence)
    Fscore = await Finance_score(sentence)
    Pjscore = await Project_score(sentence)

    similar_dict = {
        'Clerks': Cscore,
        'Marketing': Mscore,
        'Product': Pscore,
        'Finance': Fscore,
        'Project': Pjscore
    }

    return similar_dict