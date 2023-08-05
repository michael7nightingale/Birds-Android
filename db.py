from datetime import datetime
from pony.orm import Database, Required, PrimaryKey, commit, db_session, Set
from typing import Type
from uuid import uuid4

from base import BaseRepository


COLORS = {
    "orange": "#f07a19",
    "brown": "#896415",
    "black": "#000000",
    "white": "#ffffff",
    "red": "#e53838",
    "grey": "#989090",

}

db = Database()


class Bird(db.Entity):
    """Bird model."""
    id = PrimaryKey(str, default=lambda: str(uuid4()))
    name = Required(str)
    description = Required(str)
    feather_color = Required(str)
    seen_acts = Set("SeenAct")
    picture = Required(str)     # represents file path


class BirdRepository(BaseRepository):
    """Bird repository class."""
    entity: Type[db.Entity] = Bird

    @classmethod
    @db_session
    def create(cls, name: str, feather_color: str, description: str, picture=None) -> db.Entity:
        bird = cls.entity(
            name=name,
            feather_color=feather_color,
            description=description,
            picture=picture
        )
        commit()
        return bird


class SeenAct(db.Entity):
    """Seen act model."""
    id = PrimaryKey(str, default=lambda: str(uuid4()))
    bird = Required(Bird)
    time_seen = Required(datetime, default=lambda: datetime.now())


class SeenActRepository(BaseRepository):
    """Seen bird act repository class."""
    entity: Type[db.Entity] = SeenAct

    @classmethod
    @db_session
    def create(cls, bird_id: str) -> db.Entity:
        seen_act = cls.entity(bird=bird_id)
        commit()
        return seen_act

    @classmethod
    @db_session
    def get_acts_by_bird(cls, bird_id: str) -> db.Entity:
        return cls.entity.select(lambda act: act.bird == bird_id)


# bing engine and create schemas
db.bind('sqlite', 'db4.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
