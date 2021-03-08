from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField,
)


class Adoptable(Document):
    meta = {'collection': 'adoptable'}
    repository = StringField()
