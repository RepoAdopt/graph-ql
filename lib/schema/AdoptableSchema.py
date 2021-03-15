import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from lib.model.AdoptableModel import Adoptable as AdoptableModel


class Adoptable(MongoengineObjectType):
    class Meta:
        model = AdoptableModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    all_adoptables = MongoengineConnectionField(Adoptable)

schema = graphene.Schema(query=Query)
