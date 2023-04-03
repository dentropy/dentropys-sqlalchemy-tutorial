from db import session, People, Tasks, Logs
import datetime

now = datetime.datetime.now()
session.add(People("Fred", now))
session.add(People("Mary", now))
session.add(People("George", now))
session.add(People("Lucy", now))
session.commit()
