import sqlite3
from pathlib import Path

Path("data/db").mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect("data/db/bluestock_mf.db")
with open("sql/schema.sql", "r") as f:
    schema_sql = f.read()

conn.executescript(schema_sql)
conn.commit()

cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables created:", [row[0] for row in cursor.fetchall()])

conn.close()