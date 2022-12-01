#!/usr/bin/python3
from os import getenv
from models import *
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            cities = models.storage.all('City').value()
            all_cities = [city for city in cities if city.state_id == self.id]
            return all_cities

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)

