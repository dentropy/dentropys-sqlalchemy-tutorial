import os
from pprint import pprint
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine_path = "sqlite+pysqlite:///" + "/".join(os.getcwd().split("/")) + "/chinook.db"
engine = create_engine(engine_path, echo=True)
session = Session(engine)

Base = automap_base()
Base.metadata.create_all(engine)

Base.prepare(engine, reflect=True)

for table in Base.classes:
  print(table)

albums        = Base.classes.albums
artists       = Base.classes.artists
customers     = Base.classes.customers
employees     = Base.classes.employees
genres        = Base.classes.genres
invoice_items = Base.classes.invoice_items
invoices      = Base.classes.invoices
tracks        = Base.classes.tracks
media_types   = Base.classes.media_types
playlists     = Base.classes.playlists


results = session.query(invoice_items, tracks).join(tracks)

for invoice_t, tracks_t in results:
  temp_dict = {}
  table = invoice_t
  for i in range(len(table.__table__.columns.keys())):
    column = (table.__table__.columns.keys())[i]
    temp_dict[ column ] = table.__dict__[  column  ]
  temp_dict2 = {}
  table = tracks_t
  for i in range(len(table.__table__.columns.keys())):
    column = (table.__table__.columns.keys())[i]
    temp_dict2[ column ] = table.__dict__[  column  ]
  print("invoice_t", temp_dict)
  print("tracks_t ",  temp_dict2)



print(invoice_items.__table__.columns.keys())
print(tracks.__table__.columns.keys())
print(invoice_items.__table__.columns.keys())