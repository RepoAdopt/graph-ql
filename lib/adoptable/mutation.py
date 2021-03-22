import graphene

from .type import AdoptableType
from .model import Adoptable


class CreateAdoptable(graphene.Mutation):

    adoptable = graphene.Field(AdoptableType)

    class Arguments:
        repository = graphene.String()
        description = graphene.String()

    def mutate(root, info, repository, description):
        adoptable = Adoptable(repository=repository, description=description)
        adoptable.save()

        return CreateAdoptable(adoptable=adoptable)


class Mutation:
    create_adoptable = CreateAdoptable.Field()
