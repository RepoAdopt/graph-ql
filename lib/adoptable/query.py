import graphene

from .model import Adoptable
from .type import AdoptableType


class Query:
    adoptable = graphene.List(
        AdoptableType,
        page=graphene.Int(),
        limit=graphene.Int()
    )

    def resolve_adoptable(self, info, page, limit):
        if limit > 100:
            limit = 100

        adoptables_to_skip = page * limit
        return list(Adoptable.objects.order_by('-id').skip(adoptables_to_skip).limit(limit))
