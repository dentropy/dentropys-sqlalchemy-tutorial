from db import engine, session, People, Tasks, Logs
from pprint import pprint

query   = session.query(People).limit(10)
columns = [column.name for column in People.__table__.columns]
result = [dict(row) for row in query.with_entities(*[getattr(People, column) for column in columns])]
pprint(result)