import json

from db import BirdRepository, COLORS
from hashmap import HashMap


class Birds:
    """All birds list view screen."""

    @classmethod
    def on_start(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        # birds_list = {
        #     "customcards": {
        #         "layout": {
        #             "type": "LinearLayout",
        #             "orientation": "vertical",
        #             "height": "match_parent",
        #             "width": "match_parent",
        #             "weight": "0",
        #             "Elements": [
        #                 {
        #                     "type": "LinearLayout",
        #                     "orientation": "horizontal",
        #                     "height": "wrap_content",
        #                     "width": "match_parent",
        #                     "weight": "0",
        #                     "Elements": [
        #                         {
        #                             "type": "Picture",
        #                             "show_by_condition": "",
        #                             "Value": "@pic",
        #                             "NoRefresh": False,
        #                             "document_type": "",
        #                             "mask": "",
        #                             "Variable": "",
        #                             "TextSize": "16",
        #                             "TextColor": "#DB7093",
        #                             "TextBold": True,
        #                             "TextItalic": False,
        #                             "BackgroundColor": "",
        #                             "width": "75",
        #                             "height": "75",
        #                             "weight": 0
        #                         },
        #                         {
        #                             "type": "LinearLayout",
        #                             "orientation": "vertical",
        #                             "height": "wrap_content",
        #                             "width": "match_parent",
        #                             "weight": "1",
        #                             "Elements": [
        #                                 {
        #                                     "type": "TextView",
        #                                     "show_by_condition": "",
        #                                     "Value": "@name",
        #                                     "NoRefresh": False,
        #                                     "document_type": "",
        #                                     "mask": "",
        #                                     "Variable": "",
        #                                     "TextSize": "20"
        #                                 },
        #                                 {
        #                                     "type": "TextView",
        #                                     "show_by_condition": "",
        #                                     "Value": "@feather_color",
        #                                     "NoRefresh": False,
        #                                     "document_type": "",
        #                                     "mask": "",
        #                                     "Variable": "",
        #                                     "TextSize": "30"
        #                                 }
        #                             ]
        #                         }
        #                     ]
        #                 }
        #             ]
        #         },
        #         "cardsdata": []
        #     }
        # }
        birds_list = {
            "cards": []
        }
        # _files = json.loads(hashMap.get("_files"))
        #
        # query = select(c for c in ui_global.SW_Goods)
        # list["customcards"]["cardsdata"] = []
        #
        # for record in query:
        #
        #     pic = ""
        #     if 'photo' in record.pictures:
        #
        #         p = record.pictures['photo']
        #
        #         if len(p) > 0:
        #
        #             for jf in _files:  # находим путь к файлу по идентификатору
        #                 if jf['id'] == p[0]:
        #                     if os.path.exists(jf['path']):
        #                         pic = "~" + jf['path']
        #                     break
        #
        #     list["customcards"]["cardsdata"].append(
        #         {"name": record.name, "key": record.id, "product_number": str(record.product_number),
        #          "barcode": str(record.barcode), "unit": str(record.unit), "skugroup": str(record.group),
        #          "price": record.price, "unique": record.unique, "pictures": json.dumps(record.pictures), "pic": pic})

        for bird in BirdRepository.all():
            birds_list["cards"].append(
                {
                    "key": bird.id,
                    "picture": "",
                    "description": "Click to read more...",
                    "items": [
                        {
                            "key": "",
                            "value": bird.name,
                            "size": "25",
                            "color": "#1b31c2",
                            "caption_size": "12",
                            "caption_color": "#1b31c2"
                        },
                        {
                            "key": "Color",
                            "value": bird.feather_color,
                            "size": "15",
                            "color": COLORS.get(bird.feather_color, "#000000")
                        }
                    ]
                },
            )

        hashMap.put("birds_list", json.dumps(birds_list))
        return hashMap

    @classmethod
    def on_input(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        listener = hashMap.get("listener")
        if listener == 'ON_BACK_PRESSED':
            hashMap.put("ShowScreen", "Menu")
        elif hashMap.get("listener") == "CardsClick":
            hashMap.put("bird_id", hashMap.get("selected_card_key"))
            hashMap.put("ShowScreen", "Detail")
        return hashMap
