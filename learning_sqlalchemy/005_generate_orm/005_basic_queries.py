import os
from pprint import pprint
from sqlalchemy.ext.automap import automap_base

from sqlalchemy import create_engine

engine_path = "sqlite+pysqlite:///" + "/".join(os.getcwd().split("/")[:-1]) + "/chinook.db"
engine = create_engine(engine_path, echo=True)


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

# Basic Select
from sqlalchemy import select
query = select(albums)
results = engine.execute(query).fetchall()
for row in results:
  temp_dict = {}
  for i in range(len(albums.__table__.columns.keys())):
    temp_dict[ (albums.__table__.columns.keys())[i] ] = row[i]
  print(temp_dict)


# Select with `WHERE` and `ORDER BY`
from sqlalchemy import select
query = select(albums).where(albums.ArtistId == '22').order_by(albums.Title.desc())
results = engine.execute(query).fetchall()
for row in results:
  temp_dict = {}
  for i in range(len(albums.__table__.columns.keys())):
    temp_dict[ (albums.__table__.columns.keys())[i] ] = row[i]
  print(temp_dict)

# Count
from sqlalchemy.orm import Session
session = Session(engine)
result = session.query(playlists).count()
print("\nCount:", result)

# Insert
from sqlalchemy import insert
values_list = [
  {"Name" : "vierre cloud"},
  {"Name" : "sped up nightcore"},
  {"Name" : "Nightcore Reality"}
]
engine.execute(insert(artists), values_list)


query = select(artists).where(artists.Name == "vierre cloud")
results = engine.execute(query).fetchall()
for row in results:
  temp_dict = {}
  for i in range(len(artists.__table__.columns.keys())):
    temp_dict[ (artists.__table__.columns.keys())[i] ] = row[i]
  print(temp_dict)

print("Second Results")
from sqlalchemy import or_
results = session.query(artists).filter(
  or_( 
    artists.Name == "vierre cloud", 
    artists.Name == "sped up nightcore", 
    artists.Name == "Nightcore Reality"
  )
).all()

for Artist in results:
  print(Artist.ArtistId, Artist.Name)



# Update

stmt = artists.__table__.update().where(artists.Name == "vierre cloud").values(Name="MrSuicideSheep")
session.execute(stmt)
session.commit()

query = select(artists).where(artists.Name == "MrSuicideSheep")
results = engine.execute(query).fetchall()
for row in results:
  temp_dict = {}
  for i in range(len(artists.__table__.columns.keys())):
    temp_dict[ (artists.__table__.columns.keys())[i] ] = row[i]
  print(temp_dict)


# Delete
stmt = artists.__table__.delete().where(
  or_( 
    artists.Name == "vierre cloud", 
    artists.Name == "sped up nightcore", 
    artists.Name == "Nightcore Reality",
    artists.Name == "MrSuicideSheep"
  )
)
session.execute(stmt)
session.commit()

print("Delete Test")

query = select(artists).where(artists.Name == "MrSuicideSheep")
results = engine.execute(query).fetchall()
for row in results:
  temp_dict = {}
  for i in range(len(artists.__table__.columns.keys())):
    temp_dict[ (artists.__table__.columns.keys())[i] ] = row[i]
  print(temp_dict)