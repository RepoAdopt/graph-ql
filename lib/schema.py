import graphene


from .adoptable.mutation import Mutation as AdoptableMutation
from .match.mutation import Mutation as MatchMutation
from .chatMessage.mutation import Mutation as ChatMessageMutation

from .adoptable.query import Query as AdoptableQuery
from .match.query import Query as MatchQuery
from .chat.query import Query as ChatQuery


class Mutation(
    graphene.ObjectType, AdoptableMutation, MatchMutation, ChatMessageMutation
):
    def __init__(self) -> None:
        super().__init__()


class Query(
    graphene.ObjectType, AdoptableQuery, MatchQuery, ChatQuery
):
    def __init__(self) -> None:
        super().__init__()


schema = graphene.Schema(query=Query, mutation=Mutation)
