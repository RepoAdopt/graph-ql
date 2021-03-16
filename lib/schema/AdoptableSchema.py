import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from lib.model.AdoptableModel import Adoptable as AdoptableModel


class Adoptable(MongoengineObjectType):
    class Meta:
        model = AdoptableModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    adoptable = graphene.List(
        Adoptable,
        page=graphene.Int(),
        limit=graphene.Int()
    )

    def resolve_adoptable(self, info, page, limit):
        adoptables_to_skip = page * limit
        return list(AdoptableModel.objects.order_by('-id').skip(adoptables_to_skip).limit(limit))


schema = graphene.Schema(query=Query)
