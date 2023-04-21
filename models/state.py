#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128),
                      nullable=False)
        cities = relationship("City", cascade="all, delete",
                              backref="states")
    else:
        name = ""

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """fs getter attribute that returns City instances"""
            values_city = models.storage.all().items()
            list_city = []
            for city in values_city:
                try:
                    if city[1].state_id == self.id:
                        list_city.append(city)
                except AttributeError:
                    pass
            return list_city
