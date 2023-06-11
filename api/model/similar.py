import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel, pipeline
from curd.Classification import get_all_text
from curd.similar_sen import get_information

model_name = "D:\python2\code7\Fxxk-alogrithm\\api\model\similar\\all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)


async def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


async def score(sentences):
    encode_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model(**encode_input)
    sentences_embeddings = await mean_pooling(model_output, encode_input['attention_mask'])
    sentences_embeddings = F.normalize(sentences_embeddings, p=2, dim=1)
    similar = torch.cosine_similarity(sentences_embeddings[0], sentences_embeddings[1], dim=0)
    return similar.item()


async def get_all_similar(id, ids):
    sentence = await get_all_text(id)
    # print("*************************************************************")
    # print(sentence)
    Infos = await get_information(ids)
    similar_dict = dict()

    for info in Infos:
        jname = info['jname']
        jneed_other = info['jneed_other']
        sentences = [sentence, jneed_other]
        similar_dict[jname] = await score(sentences)

    return similar_dict
