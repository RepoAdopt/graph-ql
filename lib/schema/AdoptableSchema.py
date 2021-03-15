import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from lib.model.AdoptableModel import Adoptable as AdoptableModel


class Adoptable(MongoengineObjectType):
    class Meta:
        model = AdoptableModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    adoptables = graphene.List(Adoptable)

    def resolve_adoptables(self, info):
        return list(AdoptableModel.objects.all())

schema = graphene.Schema(query=Query)
