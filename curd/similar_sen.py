import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel, pipeline

model_name = "D:\python2\code7\Fxxk-alogrithm\\api\model\similar\\all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)


async def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


async def Clerks_score(sentence):
    Clerks = """
    接听、转接电话;接待来访人员；负责办公室的文秘、信息、机要和保密工作，做好办公室档案收集、整理工作；
    做好会议纪要；负责公司公文、信件、邮件、报刊杂志的分送；
    负责传真件的收发工作；负责办公室仓库的保管工作，做好物品出入库的登记；
    做好公司宣传专栏的组稿；按照公司印信管理规定，保管使用公章，并对其负责；
    熟练使用办公软件，处理日常办公业务，管理施工档案，有装饰公司工作经验者优先；
    具有全面的工作计划、对外沟通及应变等能力；
    """
    sentences = [sentence, Clerks]
    encode_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model(**encode_input)
    sentences_embeddings = await mean_pooling(model_output, encode_input['attention_mask'])
    sentences_embeddings = F.normalize(sentences_embeddings, p=2, dim=1)
    similar = torch.cosine_similarity(sentences_embeddings[0], sentences_embeddings[1], dim=0)
    return similar.item()


async def Marketing_score(sentence):
    Marketing = """
    根据公司发展方向及阶段性目标，制定品牌战略、推广策略等年度经营方案；
    参与各产品推广筹划方案的制定与执行；负责企业整体形象的定位与维护，建立完整的产品口碑营销方案及公司形象推广方案；
    负责与新媒体及知名媒体进行沟通，开展长期良好合作；负责制作与推广公司各类宣传资料，完善对外各类宣传通稿；
    负责为公司的知识产权、荣誉资质等进行申请、维护与宣传。熟练使用办公软件，可以独立制作表格、PPT等；
    良好的沟通能力，善于维护客户关系；有拓展、策划经验能力者
    """
    sentences = [sentence, Marketing]
    encode_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model(**encode_input)
    sentences_embeddings = await mean_pooling(model_output, encode_input['attention_mask'])
    sentences_embeddings = F.normalize(sentences_embeddings, p=2, dim=1)
    similar = torch.cosine_similarity(sentences_embeddings[0], sentences_embeddings[1], dim=0)
    return similar.item()


async def Product_score(sentence):
    Product = """
    负责产品上线前后的线上、线下的运营方案和推广工作，
    协助项目负责人对接市场、产品开发等，完成个项目目标；
    负责产品运营中与线下的各种合作，配合完成商务推广，实施项目评估和监控，
    提升用户活跃度和忠诚度；负责研究行业竞争动态，定期拜访客户，
    维护重要客户关系发现客户的需求，引导客户的业务需求，根据自身产品制定产品营销策略，
    达成既定目标；负责分析和挖掘产品运营数据、用户行为数据等重要价值信息负责跟进和整理产品用户反馈，
    协同产品经理提出产品迭代方案。主动性强，逻辑清晰，沟通能力强，
    能独立负责和落地运营项目能调动资源为运营目标服务；有较强数据分析能力、数据敏感性强。
    """
    sentences = [sentence, Product]
    encode_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model(**encode_input)
    sentences_embeddings = await mean_pooling(model_output, encode_input['attention_mask'])
    sentences_embeddings = F.normalize(sentences_embeddings, p=2, dim=1)
    similar = torch.cosine_similarity(sentences_embeddings[0], sentences_embeddings[1], dim=0)
    return similar.item()


async def Finance_score(sentence):
    Finance = """
    全面负责财务部的日常管理工作；组织制定财务方面的管理制度及有关规定，
    并监督执行；向公司提供各项财务报告和必要的财务分析；
    监控可能会对公司造成经济损失的重大经济合同；有独立处理账务和税务的能力者优先；
    有全盘账务处理，税务工作，年度汇算清缴能力者优先；公司资质和合同的归档保管工作；
    完成上级领导交代的其他日常工作任务。通晓财会专业知识，熟悉国家有关财务、会计、税收政策和实务；
    有互联网行业相关经验；原则性强，沟通能力佳，有良好的团队协作意识。
    """
    sentences = [sentence, Finance]
    encode_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model(**encode_input)
    sentences_embeddings = await mean_pooling(model_output, encode_input['attention_mask'])
    sentences_embeddings = F.normalize(sentences_embeddings, p=2, dim=1)
    similar = torch.cosine_similarity(sentences_embeddings[0], sentences_embeddings[1], dim=0)
    return similar.item()


async def Project_score(sentence):
    Project = """
    责任项目的整体管理；项目的订单下单、样板配合；
    产品批量安装的现场、质量、进度、成本的管理；
    项目的沟通协调管理和售后维护工作；工程回款及安装款结算工作；
    安装队及文明生产的管理工作；项目管理的档案化建设与管理的工作。
    熟练操作使用WORD/EXCEL/等办公软件；工作严谨、认真、细致，有良好的执行力；
    熟悉本行业的规范，具有良好沟通及协调能力；
    """
    sentences = [sentence, Project]
    encode_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model(**encode_input)
    sentences_embeddings = await mean_pooling(model_output, encode_input['attention_mask'])
    sentences_embeddings = F.normalize(sentences_embeddings, p=2, dim=1)
    similar = torch.cosine_similarity(sentences_embeddings[0], sentences_embeddings[1], dim=0)
    return similar.item()
