import graphene

from .type import MatchType
from .model import Match


class CreateMatch(graphene.Mutation):

    match = graphene.Field(MatchType)

    class Arguments:
        repository_id = graphene.String(required=True)

    def mutate(root, info, **args):
        token = info.context.token
        match = Match(**args, user=token["username"])
        match.save()

        return CreateMatch(match=match)


class DeleteMatch(graphene.Mutation):
    match = graphene.Field(MatchType)

    class Arguments:
        repository_id = graphene.String(required=True)

    def mutate(root, info, **args):
        token = info.context.token
        match = Match.objects(**args, user=token["username"])
        match.delete()

        return DeleteMatch(match=match)


class Mutation:
    create_match = CreateMatch.Field()
    delete_match = DeleteMatch.Field()
