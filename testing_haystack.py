from haystack import Finder
from haystack.database.elasticsearch import ElasticsearchDocumentStore
from haystack.reader.farm import FARMReader
from haystack.retriever.sparse import ElasticsearchRetriever
from haystack.utils import print_answers

document_store = ElasticsearchDocumentStore(
    host="192.168.8.106",
    username="",
    password="",
    index="drqa_wiki",
    # embedding_dim=768,
    # embedding_field="embedding",
)
retriever = ElasticsearchRetriever(document_store=document_store)

reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)
finder = Finder(reader, retriever)

prediction = finder.get_answers(
    question="Who is the father of Angela Merkel?", top_k_retriever=10, top_k_reader=5
)


# prediction = finder.get_answers(question="Who created the Dothraki vocabulary?", top_k_reader=5)
# prediction = finder.get_answers(question="Who is the sister of Sansa?", top_k_reader=5)

print_answers(prediction, details="minimal")
