from mongoengine import Document
from mongoengine.fields import ObjectIdField, ReferenceField, ListField

from lib.chatMessage.model import ChatMessage


class Chat(Document):
    meta = {"collection": "chats"}

    adoptable_id = ObjectIdField(required=True)
    chat_messages = ListField(ReferenceField(ChatMessage))
