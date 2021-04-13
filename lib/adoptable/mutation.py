import graphene

from .type import AdoptableType
from .model import Adoptable


class CreateAdoptable(graphene.Mutation):

    adoptable = graphene.Field(AdoptableType)

    class Arguments:
        repository = graphene.String(required=True)
        description = graphene.String(required=False)

    def mutate(root, info, token, **args):
        adoptable = Adoptable(**args, owner=token["username"])
        # TODO CHANGE SO NO DOUBLE OWNER-REPO COMBO'S CAN BE IN DATABASE
        adoptable.save()

        return CreateAdoptable(adoptable=adoptable)


class Mutation:
    create_adoptable = CreateAdoptable.Field()
