from lib.model.AdoptableModel import Adoptable

def populate():
    adoptable = Adoptable(repository="testRepo1")
    adoptable.save()
    adoptable1 = Adoptable(repository="testRepo2")
    adoptable1.save()
    adoptable1 = Adoptable(repository="testRepo3")
    adoptable1.save()