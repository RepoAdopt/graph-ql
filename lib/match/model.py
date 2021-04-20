from mongoengine import Document
from mongoengine.fields import StringField, ObjectIdField


class Match(Document):
    meta = {
        "collection": "matches",
        "indexes": [{"fields": ("repository_id", "user"), "unique": True}],
    }

    repository_id = ObjectIdField(required=True)
    user = StringField(required=True)
