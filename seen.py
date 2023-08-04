import datetime
import json

from db import SeenActRepository
from hashmap import HashMap
from base import BaseScreen


class Seen(BaseScreen):

    @classmethod
    def on_start(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        table = {
            "type": "table",
            "textsize": "18",
            "columns": [
                {
                    "name": "bird",
                    "header": "Bird",
                    "weight": "1"
                },
                {
                    "name": "time_seen",
                    "header": "Last Time",
                    "weight": "2"
                },
                {
                    "name": "amount",
                    "header": "Amount",
                    "weight": "3"
                },
            ]
        }
        # work with SQL via Pony ORM
        query = SeenActRepository.all()
        rows = {}

        for record in query:
            if record.bird.name in rows:
                rows[record.bird.name].update(
                    time_seen=record.time_seen.strftime("%H:%M - %m.%d.%Y"),
                    amount=rows[record.bird.name]['amount'] + 1
                )
            else:
                rows[record.bird.name] = (
                    {
                        "bird": record.bird.name,
                        "id": record.id,
                        "time_seen": record.time_seen.strftime("%H:%M - %m.%d.%Y"),
                        "amount": 1
                    }
                )
        table['rows'] = list(rows.values())
        hashMap.put("seen_list", json.dumps(table))
        return hashMap

    @classmethod
    def on_input(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        listener = hashMap.get("listener")
        if listener == 'ON_BACK_PRESSED':
            hashMap.put("ShowScreen", "Menu")
        elif listener == "btn_add":
            bird_selected_id = hashMap.get("bird_selected_id")
            if bird_selected_id is None:
                hashMap.put("toast", "Bird to see is not selected")
                hashMap.put("ShowScreen", "Birds")
            else:
                seen_act = SeenActRepository.create(bird_selected_id)
                if seen_act is None:
                    hashMap.put("toast", "Error while making new seen act")
                else:
                    hashMap.put("ShowScreen", "Seen")
        return hashMap
