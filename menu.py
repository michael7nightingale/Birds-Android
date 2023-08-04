from base import BaseScreen
from hashmap import HashMap


class Menu(BaseScreen):
    """Menu screen class."""

    @classmethod
    def on_start(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        return hashMap

    @classmethod
    def on_input(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        listener = hashMap.get("listener")
        if listener == "menu":
            hashMap.put("ShowScreen", hashMap.get("menu"))
        if listener == "ON_BACK_PRESSED":
            hashMap.put("FinishProcess", "")
        return hashMap
