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

        chat = Chat.objects().all()
        print(chat)

        if len(chat) != 1:
            return {}

        chat = chat[0]

        # matches = Match.objects(adoptable=chat["adoptable_id"])
        # print(matches[0].user)

        # def map_user(match):
        #     print("map")
        #     print(match.user)
        #     return match.user

        # chat.users = map(map_user, matches)
        # print(chat.users)

        adoptable = Adoptable.objects(id=chat["adoptable_id"]).all()
        chat.users = ["Niek125", "BeauTaapken"]
        # chat.users.append()
        # chat.users.append(adoptable["owner"])
        chat.users = set(chat.users)

        # if token["username"] not in chat.users:
        #     return {}

        chat.chat_messages = ChatMessage.objects(chat_id=chat["id"]).order_by(
            "timestamp"
        )

        return chat
