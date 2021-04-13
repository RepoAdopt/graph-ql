import graphene

from .type import MatchType
from .model import Match


class CreateMatch(graphene.Mutation):

    match = graphene.Field(MatchType)

    class Arguments:
        repository = graphene.String(required=True)
        user = graphene.String(required=True)

    def mutate(root, info, token, **args):
        print(token["username"])
        match = Match(**args, user=token["username"])
        match.save()

        return CreateMatch(match=match)


class Mutation:
    create_match = CreateMatch.Field()
