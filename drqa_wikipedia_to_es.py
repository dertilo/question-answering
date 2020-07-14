import os
from esutil.es_stateful_parallel_pool import setup_index, populate_es_parallel_pool
from esutil.es_util import build_es_client

if __name__ == "__main__":
    from pathlib import Path

    home = str(Path.home())

    data_path = home + "/code/question-answering"
    files = [
        data_path + "/" + f
        for f in os.listdir(data_path)
        if f.startswith("drqa") and f.endswith(".jsonl.gz")
    ]

    INDEX_NAME = "drqa_wiki"
    TYPE = "doc"

    mapping = """
    {
      "mappings": {
        "properties": {
          "id": {
            "type": "str",
            "enabled": true
          }
          "text": {
            "type": "str",
            "enabled": true
          }
        }
      }
    }
    """
    es_client = build_es_client()
    files = setup_index(
        es_client, files, INDEX_NAME, TYPE, from_scratch=True, mapping=mapping
    )

    num_processes = 8
    populate_es_parallel_pool(files, INDEX_NAME, TYPE, num_processes=num_processes)
