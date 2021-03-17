import graphene

from .type import AdoptableType
from.model import Adoptable

class CreateAdoptable(graphene.Mutation):

    adoptable = graphene.Field(AdoptableType)

    class Arguments:
        repository = graphene.String()

    def mutate(root, info, repository):
        adoptable = Adoptable(repository=repository)
        adoptable.save()

        return CreateAdoptable(adoptable=adoptable)


class Mutation:
    adoptable = CreateAdoptable.Field()
