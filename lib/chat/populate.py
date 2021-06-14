from .model import Chat

from lib.adoptable.model import Adoptable


def populate():
    chat = Chat(adoptable=Adoptable.objects[0].id)
    chat.save()
