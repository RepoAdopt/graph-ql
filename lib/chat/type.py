from graphene import List, String
from graphene_mongo import MongoengineObjectType

from .model import Chat

from lib.chatMessage.type import ChatMessageType


class ChatType(MongoengineObjectType):
    class Meta:
        model = Chat

    chat_messages = List(ChatMessageType)
    users = List(String)
