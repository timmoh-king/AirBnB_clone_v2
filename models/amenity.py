#!/usr/bin/python3

""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    __table_args__ = ({'mysql_default_charset': 'latin1'})

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=True)
