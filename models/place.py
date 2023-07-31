#!/usr/bin/python3

""" Place Module for HBNB project"""
import models
from os import getenv
from sqlalchemy import Table
from models.base_model import Base
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table


association_table = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitide = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    amenities = relationship(
        "Amenity", secondary="place_amenity", backref="place_amenities", viewonly=False)
    reviews = relationship(
        "Review", backref="place", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)

            return review_list

        @property
        def amenities(self):
            """Get/set linked Amenities."""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)

            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """Set the associated Amenities"""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
