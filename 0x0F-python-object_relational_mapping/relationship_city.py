#!/usr/bin/python3
'''Defines City model
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from relationship_state import Base


class City(Base):
    '''Models a city..

    Args:
        Base (declarative_base): sqlalchemy declarative base.
    '''
    __tablename__ = 'cities'

    id = Column(Integer(), nullable=False, autoincrement=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
