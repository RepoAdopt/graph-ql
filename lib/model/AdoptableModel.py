from mongoengine import Document
from mongoengine.fields import (
    StringField,
)


class Adoptable(Document):
    meta = {'collection': 'adoptable'}
    repository = StringField()
