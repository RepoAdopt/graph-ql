from .model import Adoptable


def populate():
    adoptable = Adoptable(repository="RepoAdopt/client", owner="Niek125")
    adoptable.save()
    adoptable1 = Adoptable(repository="RepoAdopt/graph-ql", owner="Niek125")
    adoptable1.save()
    adoptable1 = Adoptable(repository="RepoAdopt/event-handlers", owner="Niek125")
    adoptable1.save()
