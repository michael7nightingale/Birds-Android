"""
Base classes (ABC interfaces) file to make contract with inherits for implementing
necessary methods.
"""

from abc import ABC, abstractmethod
from pony.orm import db_session
from pony.orm.core import EntityMeta

from hashmap import HashMap


class BaseScreen(ABC):
    """
    Base screen handler encapsulation class. Methods are to be implemented.
    There is no instance methods because objects are not created.
    Just encapsulates screen logic.
    """
    @classmethod
    @abstractmethod
    def on_input(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        """Input event handler."""
        pass

    @classmethod
    @abstractmethod
    def on_start(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        """Start scree event handler."""
        pass


class BaseRepository(ABC):
    """
    Base repository class. Defines the simplest data access operations.
    """
    entity: EntityMeta

    @classmethod
    @abstractmethod
    def create(cls, bird_id: str):
        pass

    @classmethod
    @db_session
    def all(cls):
        return cls.entity.select()

    @classmethod
    @db_session
    def get(cls, id_: str):
        obj = cls.entity.get(id=id_)
        return obj
