from datetime import datetime

from .model import ChatMessage


def populate():
    chat_message1 = ChatMessage(
        user="BeauTaapken", message="Hi there!", timestamp=datetime.now()
    )
    chat_message2 = ChatMessage(
        user="BeauTaapken", message="I'm special.", timestamp=datetime.now()
    )
    chat_message3 = ChatMessage(
        user="Niek125", message="Good for you!", timestamp=datetime.now()
    )

    chat_message1.save()
    chat_message2.save()
    chat_message3.save()
