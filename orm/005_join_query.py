from db import engine, session, People, Tasks, Logs
from pprint import pprint

query   = session.query(People, Tasks).join(Tasks)

for row in list(query):
  formatted_result = { **row[0].__dict__, **row[1].__dict__ }
  del formatted_result["_sa_instance_state"]
  pprint(  formatted_result  )
