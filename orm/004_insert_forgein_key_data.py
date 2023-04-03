from db import session, People, Tasks, Logs
from datetime import datetime
from pprint import pprint

now = datetime.now()

# Get People's ID'session
results   = session.query(People).limit(4)
people_list = []
for result in results:
  people_list.append({
    'id'   :  result.id,
    'name' :  result.name
  })
pprint(people_list)


session.add(Tasks(
  now,
  "Make Breakfast",
  "Green Eggs and Ham",
  datetime(2030, 2, 24, 8, 15),
  people_list[0]["id"]
))

session.add(Tasks(
  now,
  "Make Lunch",
  "Sandwiches",
  datetime(2030, 2, 24, 11, 30),
  people_list[1]["id"]
))

session.add(Tasks(
  now,
  "Make Dinner",
  "Roast Beef",
  datetime(2030, 2, 24, 17, 45),
  people_list[2]["id"]
))


session.add(Tasks(
  now,
  "Go to bed",
  "Don't forget to brush teeth",
  datetime(2030, 2, 24, 23, 15),
  people_list[3]["id"]
))

session.commit()