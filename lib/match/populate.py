from .model import Match
from lib.adoptable.model import Adoptable


def populate():
    match = Match(user="Niek125", adoptable=Adoptable.objects[0].id)
    match.save()
    match1 = Match(user="BeauTaapken", adoptable=Adoptable.objects[1].id)
    match1.save()
    match2 = Match(user="Niek125", adoptable=Adoptable.objects[2].id)
    match2.save()
