#!/usr/bin/python3
""" State for HBNB  project """

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models
from os import getenv


class State(BaseModel, Base):
    """State class representation"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128),
                nullable=False)
        cities = relationship("City", cascade="all, delete",
                backref="states")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ initializing states"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ getter attribute"""
            v_city = models.storage.all("City").values()
            list_city = []
            for city in v_city:
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
