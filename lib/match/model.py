from mongoengine import Document
from mongoengine.fields import StringField, ObjectIdField


class Match(Document):
    meta = {
        "collection": "matches",
        "indexes": [{"fields": ("repository", "user"), "unique": True}],
    }

    repository = ObjectIdField(required=True)
    user = StringField(required=True)
