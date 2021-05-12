import graphene

from bson import ObjectId

from .model import Chat
from .type import ChatType

from lib.chatMessage.model import ChatMessage


class Query:
    chat = graphene.Field(ChatType, id=graphene.String())

    def resolve_chat(self, info, id):
        token = getattr(info.context, "token", None)

        if token is None:
            return []

        chat = Chat.objects.get(id=ObjectId(id))
        # TODO check if user is authorized (matched)
        chat.chat_messages = ChatMessage.objects(chat_id=chat["id"]).order_by("timestamp")

        return chat
