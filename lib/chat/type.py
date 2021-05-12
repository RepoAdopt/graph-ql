from graphene import List, 
from graphene_mongo import MongoengineObjectType

from .model import Chat


class ChatMessageType(MongoengineObjectType):
	class Meta:
			model = Chat

	# users = List()

	# def resolve_users(**kwargs):
	# 	print(kwargs)
	# 	return []
