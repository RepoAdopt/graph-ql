import graphene

from .model import Match
from .type import MatchType


class Query:
    my_matches = graphene.List(MatchType)

    def resolve_my_matches(self, info):
        token = getattr(info.context, "token", None)
        if token is not None:
            match = Match.objects(user=token["username"])
            return list(match)
        return list()
