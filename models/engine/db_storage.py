#!/usr/bin/python3

"""
    New engine DBStorage: (models/engine/db_storage.py)
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """
        Private class attributes
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            Public instance methods:
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    # def all(self, cls=None):
    #     """
    #         all objects depending of the class name (argument cls)
    #     """
    #     if cls is None:
    #         obj = self.__session.query(User).all()
    #         obj.extend(self.__session.query(State).all())
    #         obj.extend(self.__session.query(City).all())
    #         obj.extend(self.__session.query(Amenity).all())
    #         obj.extend(self.__session.query(Place).all())
    #         obj.extend(self.__session.query(Review).all())
    #     else:
    #         if type(cls) == str:
    #             cls = eval(cls)
    #         obj = self.__session.query(cls)
    #     return {"{}.{}".format(type(o).__name__, o.id): o for o in obj}

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in cls:
            if cls is None or cls is cls['clss'] or cls is clss:
                objs = self.__session.query(cls[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and refresh the db"""
        Base.metadata.create_all(self.__engine)
        session_reload = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_reload)
        self.__session = Session()

    def close(self):
        """Close the SQLAlchemy working session"""
        self.__session.close()
