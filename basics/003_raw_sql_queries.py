from sqlalchemy import create_engine
import os


engine_path = "sqlite+pysqlite:///" + "/".join(os.getcwd().split("/")) + "/chinook.db"
engine = create_engine(engine_path, echo=True)

my_query = 'SELECT * FROM playlists'
results = engine.execute(my_query).fetchall()

from pprint import pprint
pprint(results)