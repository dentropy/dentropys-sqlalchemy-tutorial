import os
import graphviz # Requirement for sqlalchemy_schemadisplay graph.write_png
from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy import MetaData

engine_path = "sqlite+pysqlite:///" + "/".join(os.getcwd().split("/")) + "/chinook.db"
graph = create_schema_graph(metadata=MetaData(engine_path))
graph.write_png(os.getcwd() + '/my_erd.png')