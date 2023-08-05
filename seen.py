import json

from db import SeenActRepository
from hashmap import HashMap
from base import BaseScreen


class Seen(BaseScreen):
    """Seen birds list screen."""

    @classmethod
    def on_start(cls, hashMap: HashMap, _files=None, _data=None) -> HashMap:
        table = {
            "type": "table",
            "textsize": "18",
            "columns": [
                {
                    "name": "bird",
                    "header": "Bird",
                    "weight": "2"
                },
                {
                    "name": "time_seen",
                    "header": "Last Time",
                    "weight": "2"
                },
                {
                    "name": "amount",
                    "header": "Amount",
                    "weight": "1"
                },
            ]
        }
        query = SeenActRepository.all()
        rows = {}
        # here we go through all records and count amount of each bird seen act in O(N)
        # we remind the last time seen the bird, queryset is already ordered by time
        for record in query:
            if record.bird.id in rows:
                rows[record.bird.id].update(
                    time_seen=record.time_seen.strftime("%H:%M - %m.%d.%Y"),
                    amount=rows[record.bird.id]['amount'] + 1
                )
            else:
                rows[record.bird.id] = (
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
        return hashMap
