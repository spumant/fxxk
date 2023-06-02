from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
from curd.workexp import get_context

model_name = "api/model/work-exp/luhuachinese_pretrain_mrc_roberta_wwm_ext_large"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
qa = pipeline('question-answering', tokenizer=tokenizer, model=model)

question = ['工作年限？']


async def get_exp_year(id):
    context = get_context(id)

    length = len(context)
    start = 0
    answer = []
    flag = True
    while (start < length):
        if flag:
            context = context[start:]
            ans_dict = qa(question=question, context=context)
            # answer += "，" + ans_dict['answer']
            answer.append(ans_dict['answer'])
            if start != ans_dict['end']:
                start = ans_dict['end']
                # print(start)
            else:
                flag = False
        else:
            break

    return answer
