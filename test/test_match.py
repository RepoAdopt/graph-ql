import unittest

from mongoengine import connect, disconnect

from lib.adoptable.model import Adoptable
from lib.match.model import Match


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connect("RepoAdoptTest", host="mongomock://localhost/")

        adoptable = Adoptable(repository="testRepo", owner="test")
        adoptable.save()
        adoptable1 = Adoptable(repository="testRepo1", owner="test")
        adoptable1.save()
        match = Match(user="test", adoptable=adoptable.id)
        match.save()
        match1 = Match(user="test", adoptable=adoptable1.id)
        match1.save()

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def test_match_model(self):
        match = Match.objects().first()
        assert match.user == "Test" and match.adoptable.repository == "testRepo"
