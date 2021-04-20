from .model import Match


def populate():
    match = Match(repository_id="60756a6b2ef13b728ec4cc29", user="Niek125")
    match.save()
    match1 = Match(repository_id="60756a6b2ef13b728ec4cc2a", user="BeauTaapken")
    match1.save()
    match2 = Match(repository_id="60756a6b2ef13b728ec4cc2b", user="Niek125")
    match2.save()
