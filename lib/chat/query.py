import graphene

from bson import ObjectId

from .model import Chat
from .type import ChatType


class Query:
    chat = graphene.Field(ChatType, id=graphene.String())

    def resolve_chat(self, info, id):
        print(ObjectId(id))
        token = getattr(info.context, "token", None)

        # if token is None:
        #     return {}

        chat = Chat.objects.get(id=ObjectId(id))
        print(chat)
        # TODO check if user is authorized (matched)

        return chat
