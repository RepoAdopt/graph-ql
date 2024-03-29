import graphene

from bson import ObjectId

from datetime import datetime

from .type import ChatMessageType
from .model import ChatMessage


class PostChatMessage(graphene.Mutation):
    chat_message = graphene.Field(ChatMessageType)

    class Arguments:
        message = graphene.String(required=True)
        chat_id = graphene.String(required=True)

    def mutate(root, info, chat_id, **args):
        token = getattr(info.context, "token", None)

        if token is None:
            return {}

        chat_message = ChatMessage(
            **args, user=token["username"], timestamp=datetime.now(), chat_id=ObjectId(chat_id)
        )
        chat_message.save()
        return PostChatMessage(chat_message=chat_message)


class Mutation:
    post_chat_message = PostChatMessage.Field()
