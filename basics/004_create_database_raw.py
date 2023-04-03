from sqlalchemy import create_engine
import os
from pprint import pprint

engine_path = "sqlite+pysqlite:///" + "/".join(os.getcwd().split("/")) + "/temp.db"
engine = create_engine(engine_path, echo=True)

my_query = """
  CREATE TABLE IF NOT EXISTS scraped_urls_t (
    id               INTEGER PRIMARY KEY,
    url_id           INTEGER,
    date_scraped     DATE,
    html             TEXT
  )
"""
results = engine.execute(my_query)
pprint(results)

my_query = """
  CREATE TABLE IF NOT EXISTS urls_t(
    id               INTEGER PRIMARY KEY,
    full_url         TEXT,
    url_schema       TEXT,
    domain           TEXT,
    path             TEXT,
    params           TEXT,
    query            TEXT,
    fragment         TEXT
  )
"""
results = engine.execute(my_query)
pprint(results)

my_query = """
  select name
  from sqlite_master 
  where type='table'
"""
results = engine.execute(my_query).fetchall()
pprint(results)

my_query = """
  PRAGMA table_info(scraped_urls_t);
"""
results = engine.execute(my_query).fetchall()
pprint(results)

my_query = """
  PRAGMA table_info(urls_t);
"""
results = engine.execute(my_query).fetchall()
pprint(results)
