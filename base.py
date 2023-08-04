from abc import ABC, abstractmethod
from typing import Type
from pony.orm import Database, db_session
from pony.orm.core import Entity, EntityMeta

from hashmap import HashMap


class BaseScreen(ABC):
    """
    Base screen handler encapsulation class. Methods are to be implemented.
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
    """Base repository class."""
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
