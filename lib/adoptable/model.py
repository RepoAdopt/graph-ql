from mongoengine import Document
from mongoengine.fields import StringField, ObjectIdField


class Adoptable(Document):
    meta = {
        "collection": "adoptables",
        "indexes": [{"fields": ("repository", "owner"), "unique": True}],
    }
    repository = StringField(required=True)
    description = StringField(required=False)
    owner = StringField(required=True)
