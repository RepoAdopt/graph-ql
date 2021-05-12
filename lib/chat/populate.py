from .model import Chat

from lib.adoptable.model import Adoptable


def populate():
    chat = Chat(adoptable_id=Adoptable.objects.first()["id"])
    chat.save()
