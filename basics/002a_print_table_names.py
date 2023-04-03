from sqlalchemy import create_engine
import os

engine_path = "sqlite+pysqlite:///" + "/".join(os.getcwd().split("/")) + "/chinook.db"
engine = create_engine(engine_path, echo=True)

from sqlalchemy import inspect
inspector = inspect(engine)
schemas = inspector.get_schema_names()

for schema in schemas:
    print("schema: %s" % schema)
    for table_name in inspector.get_table_names(schema=schema):
        print(table_name)
