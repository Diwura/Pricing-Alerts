from abc import ABCMeta, abstractmethod
from typing import List
from common.database import Database

class Model(metaclass=ABCMeta):
    collection = "models"

    def __init__(self, *args, **kwargs):
        pass
    @abstractmethod #to ensure that the method with the abstract method decorator is implemented by the subclass that inherits from Model class.
    def json(self):
        raise NotImplementedError

    @classmethod
    def all(cls) -> List:
        elements_from_db = Database.find(cls.collection,{})
        return [cls(**elem) for elem in elements_from_db] #this is possible becuase the objects were saved into the database using the format in which objects from the item and alert class are created.
        #now instead of a cursor of dictionaries we get a list of item objects on which we can directly carry out methods.

        

 