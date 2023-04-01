from sqlalchemy import create_engine
import os
from pprint import pprint

engine_path = "sqlite+pysqlite:///" + "/".join(os.getcwd().split("/")) + "/chinook.db"
engine = create_engine(engine_path, echo=True)

# Select

# Select with where

# Count

# Update

# Delete