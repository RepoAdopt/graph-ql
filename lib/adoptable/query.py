import graphene

from .model import Adoptable
from .type import AdoptableType


class Query:
    adoptable = graphene.List(
        AdoptableType,
        page=graphene.Int(),
        limit=graphene.Int()
    )

    def resolve_adoptable(self, info, page, limit, token=None):
        limit = max(1, min(limit, 100))
        page = max(0, page)

        adoptables_to_skip = page * limit

        adoptables = None
        if token != None:
            adoptables = Adoptable.objects(owner__ne=token['username'])
        else :
            adoptables = Adoptable.objects

        return list(adoptables.order_by('-id').skip(adoptables_to_skip).limit(limit))

    my_adoptables = graphene.List(
        AdoptableType
    )

    def resolve_my_adoptables(self, info, token):
        return list(Adoptable.objects(owner=token['username']))

