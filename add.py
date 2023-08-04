import json
from typing import Tuple

from db import BirdRepository, COLORS
from base import BaseScreen
from hashmap import HashMap


def save_bird(hashMap: HashMap) -> Tuple[HashMap, bool]:
    """Function for saving bird to the database."""
    if not hashMap.containsKey("name"):
        hashMap.put("toast", "Name is unfilled")
        return hashMap, False
    else:
        name = hashMap.get("name")
        if len(name) == 0:
            hashMap.put("toast", "Name is unfilled")
            return hashMap, False

    if not hashMap.containsKey("description"):
        hashMap.put("toast", "Description is unfilled")
        return hashMap, False
    else:
        description = hashMap.get("description")
        if len(name) == 0:
            hashMap.put("toast", "Description is unfilled")
            return hashMap, False

    if not hashMap.containsKey("color"):
        hashMap.put("toast", "Color is unfilled")
        return hashMap, False
    else:
        color = hashMap.get("color")
        if len(color) == 0:
            hashMap.put("toast", "Color is unfilled")
            return hashMap, False

    bird = BirdRepository.create(
        name=name,
        feather_color=color,
        description=description,

    )
    hashMap.put("toast", "Bird saved!")
    return hashMap, True


class Add(BaseScreen):
    """Adding bird screen."""

    @classmethod
    def on_start(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        hashMap.put("mm_local", "")
        hashMap.put("mm_compression", "70")
        hashMap.put("mm_size", "65")
        hashMap.put("fill_name", json.dumps({"hint": "Bird`s name"}))
        hashMap.put("colors", ";".join(COLORS))
        return hashMap

    @classmethod
    def on_input(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        listener = hashMap.get("listener")
        if listener == "btn_save":
            hashMap, is_success = save_bird(hashMap)
            if is_success:
                hashMap.put("ShowScreen", "Menu")

        elif listener == "CardsClick":
            hashMap.put("toast", str(hashMap.get("selected_card_key")))

        elif listener == 'ON_BACK_PRESSED':
            hashMap.put("ShowScreen", "Menu")

        elif listener == 'menu_del':
            hashMap.put("ShowScreen", "Menu")
            hashMap.put("toast", "Deleted...")

        elif listener == "photo":

            # Можно вообще этого не делать-оставлять как есть. Это для примера.
            image_file = str(
                hashMap.get("photo_path"))  # "переменная"+"_path" - сюда помещается путь к полученной фотографии
            # hashMap.put("toast",str(hashMap.get("photo_path")))

            # сразу сделаем фотку - квадратной - это простой вариант. Можно сделать например отдельо миниатюры для списка, это немного сложнее

            jphotoarr = json.loads(hashMap.get("photoGallery"))
            hashMap.put("photoGallery", json.dumps(jphotoarr))
            # hashMap.put("toast",json.dumps(jphotoarr))

        elif listener == "gallery_change":  # пользователь может удалить фото из галереи. Новый массив надо поместить к документу

            if hashMap.containsKey("photoGallery"):  # эти 2 обработчика - аналогичные, просто для разных событий
                jphotoarr = json.loads(hashMap.get("photoGallery"))
                hashMap.put("photoGallery", json.dumps(jphotoarr))
                # hashMap.put("toast","#2"+json.dumps(jphotoarr))

        return hashMap
