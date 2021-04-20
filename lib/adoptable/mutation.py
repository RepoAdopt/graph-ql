import graphene

from .type import AdoptableType
from .model import Adoptable


class CreateAdoptable(graphene.Mutation):

    adoptable = graphene.Field(AdoptableType)

    class Arguments:
        repository = graphene.String(required=True)
        description = graphene.String(required=False)

    def mutate(root, info, **args):
        token = getattr(info.context, "token", None)
        if token is not None:
            adoptable = Adoptable(**args, owner=token["username"])
            adoptable.save()
            return CreateAdoptable(adoptable=adoptable)
        return {}


class Mutation:
    create_adoptable = CreateAdoptable.Field()
