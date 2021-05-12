from graphene import List
from graphene_mongo import MongoengineObjectType

from .model import Chat

from lib.chatMessage.type import ChatMessageType


class ChatType(MongoengineObjectType):
    class Meta:
        model = Chat

    chat_messages = List(ChatMessageType)

    # users = List()

    # def resolve_users(**kwargs):
    # 	print(kwargs)
    # 	return []
