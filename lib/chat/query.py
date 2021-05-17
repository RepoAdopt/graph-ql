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

        chat = Chat.objects(adoptable_id=ObjectId(adoptable_id)).all()

        if len(chat) != 1:
            return {}

        chat = chat[0]

        matches = Match.objects(adoptable=chat["adoptable_id"])
        chat.users = map(lambda match: match.user, matches)

        adoptable = Adoptable.objects.get(id=chat["adoptable_id"])
        chat.users.append(adoptable["owner"])
        chat.users = set(chat.users)

        if token["username"] not in chat.users:
            return {}

        chat.chat_messages = ChatMessage.objects(chat_id=chat["id"]).order_by(
            "timestamp"
        )

        return chat
