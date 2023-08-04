from db import BirdRepository
from base import BaseScreen
from hashmap import HashMap


class Detail(BaseScreen):
    """Detail bird view screen."""

    @classmethod
    def on_start(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        if not hashMap.containsKey("bird_id"):
            hashMap.put("toast", "Bird is not selected")
            hashMap.put("ShowScreen", "Menu")
        else:
            bird_id = hashMap.get("bird_id")
            bird = BirdRepository.get(bird_id)
            if bird is None:
                hashMap.put("toast", "Bird is not found")
                hashMap.put("ShowScreen", "Menu")
            else:
                hashMap.put("name", bird.name)
                hashMap.put("description", bird.description)
                color = f"Color: {bird.feather_color}"
                hashMap.put("feather_color", color)
        return hashMap

    @classmethod
    def on_input(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        listener = hashMap.get("listener")
        if listener == 'ON_BACK_PRESSED':
            hashMap.remove("bird_id")
            hashMap.put("ShowScreen", "Birds")
        return hashMap
