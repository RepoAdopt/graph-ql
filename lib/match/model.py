from mongoengine import Document
from mongoengine.fields import (
    StringField,
    ReferenceField,
)

from lib.adoptable.model import Adoptable


class Match(Document):
    meta = {
        "collection": "matches",
        "indexes": [{"fields": ("adoptable", "user"), "unique": True}],
    }

    user = StringField(required=True)
    adoptable = ReferenceField(Adoptable)
