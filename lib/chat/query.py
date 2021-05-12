import graphene

from bson import ObjectId

from .model import Chat
from .type import ChatType

from lib.chatMessage.model import ChatMessage


class Query:
    chat = graphene.Field(ChatType, adoptable_id=graphene.String())

    def resolve_chat(self, info, adoptable_id):
        token = getattr(info.context, "token", None)

        # if token is None:
        #     return {}

        chat = Chat.objects.get(adoptable_id=ObjectId(adoptable_id))
        # TODO check if user is authorized (matched)
        chat.chat_messages = ChatMessage.objects(chat_id=chat["id"]).order_by("timestamp")

        return chat
