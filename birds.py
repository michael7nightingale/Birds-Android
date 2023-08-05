import json

from db import BirdRepository, COLORS
from hashmap import HashMap


class Birds:
    """All birds list view screen."""

    @classmethod
    def on_start(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        birds_list = {
            "customcards": {
                "options": {
                    "search_enabled": True,
                    "save_position": True
                },
                "layout": {
                    "type": "LinearLayout",
                    "orientation": "vertical",
                    "height": "match_parent",
                    "width": "match_parent",
                    "weight": "0",
                    "Elements": [
                        {
                            "type": "LinearLayout",
                            "orientation": "horizontal",
                            "height": "wrap_content",
                            "width": "match_parent",
                            "weight": "0",
                            "Elements": [
                                {
                                    "type": "Picture",
                                    "show_by_condition": "",
                                    "Value": "@picture",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": "",
                                    "TextSize": "16",
                                    "TextColor": "#DB7093",
                                    "TextBold": True,
                                    "TextItalic": False,
                                    "BackgroundColor": "",
                                    "width": "75",
                                    "height": "75",
                                    "weight": 0
                                },
                                {
                                    "type": "LinearLayout",
                                    "orientation": "vertical",
                                    "height": "wrap_content",
                                    "width": "match_parent",
                                    "weight": "1",
                                    "Elements": [
                                        {
                                            "type": "TextView",
                                            "show_by_condition": "",
                                            "Value": "@name",
                                            "NoRefresh": False,
                                            "document_type": "",
                                            "mask": "",
                                            "Variable": "",
                                            "TextSize": "30"
                                        },
                                        {
                                            "type": "TextView",
                                            "show_by_condition": "",
                                            "Value": "@feather_color",
                                            "NoRefresh": False,
                                            "document_type": "",
                                            "mask": "",
                                            "Variable": "",
                                            "TextSize": "18",
                                            "TextColor": "@color"
                                        },
                                    ]
                                }
                            ]
                        }
                    ]
                },
                "cardsdata": []
            }
        }

        for bird in BirdRepository.all():
            birds_list['customcards']['cardsdata'].append(
                {
                    "key": bird.id,     # needed on CardsClick event
                    "name": f"Name: {bird.name}",
                    "feather_color": f"Feather color: {bird.feather_color}",
                    "picture": f"~{bird.picture}",
                    "color": COLORS[bird.feather_color],
                }
            )

        hashMap.put("birds_list", json.dumps(birds_list))
        return hashMap

    @classmethod
    def on_input(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        listener = hashMap.get("listener")
        if listener == 'ON_BACK_PRESSED':
            hashMap.put("ShowScreen", "Menu")
        elif listener == "CardsClick":
            hashMap.put("bird_id", hashMap.get("selected_card_key"))
            hashMap.put("ShowScreen", "Detail")
        return hashMap
