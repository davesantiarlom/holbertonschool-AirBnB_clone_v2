#!/usr/bin/python3
"""
DBStorage, for database usage
"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ This class interacts with the MySQL database
        to perform various actions """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialization of various variables """
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, passwd, host, db),
                                      pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        This does not work as intended. For whatever reason cls is still
        holding None even if a class was passed in
        """
        object_list = []
        # print(cls)
        if cls is not None:
            # print("Cls only")
            object_list = self.__session.query(cls)
        else:
            # print("Everything!")
            classes = [State, City, User, Place, Review, Amenity]
            for x in classes:
                object_list += self.__session.query(x).all()
                # print(object_list)
                # print("")

        my_dict = {}
        for obj in object_list:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """ Adds the object to the database """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """ Saves any changes to the database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete the obj from the database """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Reloads data from the database using session """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(expire_on_commit=False,
                                      bind=self.__engine)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        """ Call remove() method on private session attribute """
        self.__session.close()
