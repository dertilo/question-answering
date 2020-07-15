from pprint import pprint
from haystack.database.elasticsearch import ElasticsearchDocumentStore
from haystack.retriever.sparse import ElasticsearchRetriever

if __name__ == '__main__':

    document_store = ElasticsearchDocumentStore(
        host="192.168.8.106",
        username="",
        password="",
        index="drqa_wiki",
    )

    retriever = ElasticsearchRetriever(document_store=document_store)
    while True:
        q = input("utter question: ")
        documents = retriever.retrieve(q, top_k=3)
        pprint([d.text for d in documents])