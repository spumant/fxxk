from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from curd.Classification import get_all_text, get_work_cla_dict, get_tag_dict, get_candidate
from curd.workexp import get_context

model_name = "D:\python2\code7\Fxxk-alogrithm\\api\model\class\\xlm-roberta-large-xnli-anli"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)


async def work_classification(id, ids):
    candidate_labels = await get_candidate(ids)
    text = await get_all_text(id)
    work_cla = classifier(text, candidate_labels)
    work_dict = await get_work_cla_dict(work_cla)
    return work_dict


async def tag_classification(id):
    candidate_labels = ["工作变动稳定", "工作变动频繁"]
    work = await get_context(id)
    tag_cla = classifier(work, candidate_labels)
    tag_dict = await get_tag_dict(tag_cla)
    return tag_dict
