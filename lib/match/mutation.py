import graphene

from .type import MatchType
from .model import Match


class CreateMatch(graphene.Mutation):

    match = graphene.Field(MatchType)

    class Arguments:
        repository = graphene.String(required=True)

    def mutate(root, info, token, **args):
        # TODO CHANGE SO NO DOUBLE USER-REPO COMBO'S CAN BE IN DATABASE
        match = Match(**args, user=token["username"])
        match.save(match, upsert=True)

        return CreateMatch(match=match)


class Mutation:
    create_match = CreateMatch.Field()
