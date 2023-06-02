from curd.Classification import get_all_text
from curd.similar_sen import Clerks_score, Marketing_score, Product_score, Finance_score, Project_score


async def get_all_similar(id):
    sentence = get_all_text(id)
    Cscore = Clerks_score(sentence)
    Mscore = Marketing_score(sentence)
    Pscore = Product_score(sentence)
    Fscore = Finance_score(sentence)
    Pjscore = Project_score(sentence)

    similar_dict = {
        'Clerks': Cscore,
        'Marketing': Mscore,
        'Product': Pscore,
        'Finance': Fscore,
        'Project': Pjscore
    }

    return similar_dict