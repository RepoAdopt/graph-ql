from graphene.relay import Node
from graphene_mongo import MongoengineObjectType

from .model import Adoptable


class AdoptableType(MongoengineObjectType):
    class Meta:
        model = Adoptable
        interfaces = (Node,)
