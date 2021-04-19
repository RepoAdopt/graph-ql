import graphene

from bson import ObjectId
from .type import MatchType
from .model import Match


class CreateMatch(graphene.Mutation):

    match = graphene.Field(MatchType)

    class Arguments:
        adoptable = graphene.String(required=True)

    def mutate(root, info, **args):
        token = getattr(info.context, "token", None)
        if token is not None:
            ObjectId(args.get("adoptable"))
            match = Match(**args, user=token["username"])
            match.save()
            return CreateMatch(match=match)
        return {}


class DeleteMatch(graphene.Mutation):

    match = graphene.Field(MatchType)

    class Arguments:
        adoptable = graphene.String(required=True)

    def mutate(root, info, **args):
        token = getattr(info.context, "token", None)
        if token is not None:
            match = Match.objects.get(**args, user=token["username"])
            match.delete()
            return DeleteMatch(match=match)
        return {}


class Mutation:
    create_match = CreateMatch.Field()
    delete_match = DeleteMatch.Field()
