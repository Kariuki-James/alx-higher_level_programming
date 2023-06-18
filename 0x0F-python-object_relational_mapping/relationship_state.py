#!/usr/bin/python3
'''Defines State model
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    '''Models a state.

    Args:
        Base (declarative_base): sqlalchemy declarative base.
    '''
    __tablename__ = 'states'

    id = Column(Integer(), nullable=False, autoincrement=True,
                primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref='state',
                          cascade="all, delete, delete-orphan")
