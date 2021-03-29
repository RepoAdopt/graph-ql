import graphene

from .type import AdoptableType
from .model import Adoptable


class CreateAdoptable(graphene.Mutation):

    adoptable = graphene.Field(AdoptableType)

    class Arguments:
        repository = graphene.String(required=True)
        description = graphene.String(required=False)

    def mutate(root, info, repository, description=''):
        print(root)
        print(info)

        adoptable = Adoptable(repository=repository, description=description)
        adoptable.save()

        return CreateAdoptable(adoptable=adoptable)


class Mutation:
    create_adoptable = CreateAdoptable.Field()
