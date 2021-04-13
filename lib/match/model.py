from mongoengine import Document
from mongoengine.fields import StringField, ObjectIdField


class Match(Document):
    meta = {"collection": "matches"}
    repository = ObjectIdField(required=True)
    user = StringField(required=True)
