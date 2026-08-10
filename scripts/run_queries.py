import sqlite3
import pandas as pd

conn = sqlite3.connect("data/db/bluestock_mf.db")

with open("sql/queries.sql", "r") as f:
    content = f.read()

queries = [q.strip() for q in content.split(";") if q.strip()]

for i, q in enumerate(queries, 1):
    print(f"\n{'='*60}\nQuery {i}\n{'='*60}")
    try:
        df = pd.read_sql_query(q, conn)
        print(df.head(10))
    except Exception as e:
        print("ERROR:", e)

conn.close()