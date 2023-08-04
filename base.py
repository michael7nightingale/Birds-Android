from abc import ABC, abstractmethod

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
