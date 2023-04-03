from db import engine, session, People, Tasks, Logs
from pprint import pprint

query   = session.query(People).limit(10)
for result in query:
  pprint(result.__dict__)

