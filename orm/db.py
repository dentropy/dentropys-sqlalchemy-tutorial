import os
from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine_path = "sqlite+pysqlite:///" + "/".join(os.getcwd().split("/")) + "/orm_test.db"
engine = create_engine(engine_path, echo=True)

Base = declarative_base()

class People(Base):
   __tablename__ = 'people_t'
   id = Column(Integer, primary_key=True)

   name          = Column(String)
   date_added    = Column(Date)
   def __init__(self, name, date_added):
        self.name       = name
        self.date_added = date_added


class Tasks(Base):
   __tablename__ = 'tasks_t'
   id = Column(Integer, primary_key=True)

   date_task_created  = Column(Date)
   title              = Column(String)
   description        = Column(String)
   task_due           = Column(Date)
   assignee            = Column(Integer, ForeignKey('people_t.id'))
   def __init__(self, date_task_created, title, description, task_due, assignee):
      self.date_task_created = date_task_created
      self.title             = title
      self.description       = description
      self.task_due          = task_due
      self.assignee          = assignee


class Logs(Base):
   __tablename__ = 'logs_t'
   id = Column(Integer, primary_key=True)

   task_id          = Column(Integer, ForeignKey('tasks_t.id'))
   person_logging   = Column(Integer, ForeignKey('people_t.id'))
   date_logged      = Column(Date)
   body             = Column(Text)
   body_format      = Column(String)


Base.metadata.create_all(engine)
session = Session(engine)