import graphene

from bson import ObjectId

from .model import Chat
from .type import ChatType

from lib.chatMessage.model import ChatMessage
from lib.match.model import Match
from lib.adoptable.model import Adoptable


class Query:
    chat = graphene.Field(ChatType, adoptable_id=graphene.String())

    def resolve_chat(self, info, adoptable_id):
        token = getattr(info.context, "token", None)

        if token is None:
            return {}

        adoptable = Adoptable.objects(id=ObjectId(adoptable_id)).all()

        if len(adoptable) != 1:
            return {}
        
        adoptable = adoptable[0]
        chat = Chat.objects(adoptable=adoptable).all()
        chat.adoptable = adoptable

        if len(chat) != 1:
            return {}

        chat = chat[0]

        users = list(Match.objects(adoptable=adoptable.id).values_list("user"))
        users.append(adoptable["owner"])
        chat.users = set(users)

        if token["username"] not in chat.users:
            return {}

        chat.chat_messages = ChatMessage.objects(chat_id=chat["id"]).order_by(
            "timestamp"
        )

        return chat
