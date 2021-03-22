from mongoengine import Document
from mongoengine.fields import (
    StringField,
)


class Adoptable(Document):
    meta = {'collection': 'adoptables'}
    repository = StringField(required=True)
    description = StringField()
