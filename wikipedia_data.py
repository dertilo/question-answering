from sqlalchemy import select
from sqlalchemy.sql.functions import count
from sqlutil.sqlalchemy_methods import (
    get_sqlalchemy_base_engine,
    get_rows,
    get_tables_by_reflection,
    count_rows,
)
from tqdm import tqdm
from util import data_io, util_methods

if __name__ == "__main__":
    # file = "sqlite:////home/tilo/tilo-tub/code/DrQA/data/wikipedia/docs.db"
    file = "sqlite:////home/tilo/code/DrQA/data/wikipedia/docs.db"
    base, engine = get_sqlalchemy_base_engine(file)
    tables = get_tables_by_reflection(base.metadata, engine)
    docs_table = tables["documents"]

    with engine.connect() as conn:
        num_rows = count_rows(engine, docs_table)
        num_batches = 8
        batch_size = num_rows // num_batches + 1
        it = iter(tqdm(get_rows(conn, select([docs_table]))))

        def row_gen():
            for k in range(batch_size):
                try:
                    d = next(it)
                except StopIteration as e:  # there is no next element in iterator
                    break
                yield d

        for batch_idx in range(num_batches):
            data_io.write_jsonl(
                f"drqa_wikipedia_{batch_idx}.jsonl.gz", row_gen(), mode="ab"
            )
