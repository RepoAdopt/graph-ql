from mongoengine import Document
from mongoengine.fields import ReferenceField

from lib.adoptable.model import Adoptable


class Chat(Document):
    meta = {"collection": "chats"}

    adoptable = ReferenceField(Adoptable)
