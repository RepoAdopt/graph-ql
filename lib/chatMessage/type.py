from graphene_mongo import MongoengineObjectType

from .model import ChatMessage


class ChatMessageType(MongoengineObjectType):
    class Meta:
        model = ChatMessage
