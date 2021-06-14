from lib.adoptable.populate import populate as adoptable
from lib.match.populate import populate as match
from lib.chat.populate import populate as chat
from lib.chatMessage.populate import populate as chatMessages


def populate():
    adoptable()
    match()
    chat()
    chatMessages()
