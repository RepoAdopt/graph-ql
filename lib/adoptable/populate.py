from .model import Adoptable


def populate():
    adoptable = Adoptable(repository="RepoAdopt/client")
    adoptable.save()
    adoptable1 = Adoptable(repository="RepoAdopt/graph-ql")
    adoptable1.save()
    adoptable1 = Adoptable(repository="RepoAdopt/event-handlers")
    adoptable1.save()
