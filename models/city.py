#!/usr/bin/python3

""" City Module for HBNB project """
import models
from models.base_model import Base
from models.base_model import BaseModel
from models.place import Place
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    __table_args__ = ({'mysql_default_charset': 'latin1'})

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    places = relationship("Place", backref="cities")
