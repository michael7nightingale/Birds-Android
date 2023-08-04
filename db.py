from pony.orm import Database, Required, PrimaryKey, commit, db_session, Optional
from typing import Type, Optional as OptionalType
from uuid import uuid4


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
    # picture = Optional(str)


class BirdRepository:
    """Bird repository class."""
    entity: Type[db.Entity] = Bird

    @classmethod
    @db_session
    def create(cls, name: str, feather_color: str, description: str, picture=None) -> db.Entity:
        bird = cls.entity(
            name=name,
            feather_color=feather_color,
            description=description,

        )
        commit()
        return bird

    @classmethod
    @db_session
    def all(cls):
        for bird in cls.entity.select():
            yield bird

    @classmethod
    @db_session
    def get(cls, id_: str) -> OptionalType[db.Entity]:
        bird = Bird.get(id=id_)
        return bird


# bing engine and create schemas
db.bind('sqlite', 'db1.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
