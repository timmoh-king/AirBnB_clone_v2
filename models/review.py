#!/usr/bin/python3

""" Review module for the HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    __table_args__ = ({'mysql_default_charset': 'latin1'})

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
