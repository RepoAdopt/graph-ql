from mongoengine import Document
from mongoengine.fields import StringField, DateTimeField, ObjectIdField


class ChatMessage(Document):
    meta = {"collection": "chatmessages"}

    user = StringField(required=True)
    message = StringField(required=True)
    timestamp = DateTimeField(required=False)
    chat_id = ObjectIdField(required=True)
