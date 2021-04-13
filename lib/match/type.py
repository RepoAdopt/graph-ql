from graphene.relay import Node
from graphene_mongo import MongoengineObjectType

from .model import Match


class MatchType(MongoengineObjectType):
    class Meta:
        model = Match
        interfaces = (Node,)
