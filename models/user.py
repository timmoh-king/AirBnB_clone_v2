#!/usr/bin/python3

"""This module defines a class User"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    __table_args__ = ({'mysql_default_charset': 'latin1'})

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
