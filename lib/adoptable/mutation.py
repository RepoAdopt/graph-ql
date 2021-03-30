import json
import graphene

from jwcrypto.jws import JWS

from .type import AdoptableType
from .model import Adoptable


class CreateAdoptable(graphene.Mutation):

    adoptable = graphene.Field(AdoptableType)

    class Arguments:
        repository = graphene.String(required=True)
        description = graphene.String(required=False)

    def mutate(root, info, **args):
        token = JWS()
        token.deserialize(info.context.headers['Authorization'].removeprefix('Bearer '))
        
        byte_payload = token.objects.pop('payload')
        json_payload = byte_payload.decode('UTF-8')
        payload = json.loads(json_payload)

        adoptable = Adoptable(**args, owner=payload['username'])
        adoptable.save()

        return CreateAdoptable(adoptable=adoptable)


class Mutation:
    create_adoptable = CreateAdoptable.Field()
