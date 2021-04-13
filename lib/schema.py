import graphene


from .adoptable.mutation import Mutation as AdoptableMutation
from .match.mutation import Mutation as MatchMutation

from .adoptable.query import Query as AdoptableQuery


class Mutation(graphene.ObjectType, AdoptableMutation, MatchMutation):
    def __init__(self) -> None:
        super().__init__()


class Query(graphene.ObjectType, AdoptableQuery):
    def __init__(self) -> None:
        super().__init__()


schema = graphene.Schema(query=Query, mutation=Mutation)
