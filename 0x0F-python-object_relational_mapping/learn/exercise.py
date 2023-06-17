#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Network(Base):
    __tablename__ = 'network'

    network_id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)

Base.metadata.create_all(engine)
print("========================")

net1 = Network(name="first_object")
net2 = Network(name="second_object")
net3 = Network(name="third_object")

session.add_all([net1, net2, net3])
session.flush()
