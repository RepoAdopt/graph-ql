import unittest

from mongoengine import connect, disconnect

from lib.adoptable.model import Adoptable
from lib.match.model import Match


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connect("RepoAdoptTest", host="mongomock://localhost/")

        adoptable = Adoptable(repository="testRepo", owner="Test")
        adoptable.save()
        adoptable1 = Adoptable(repository="testRepo1", owner="Test")
        adoptable1.save()
        match = Match(user="Test", adoptable=adoptable.id)
        match.save()
        match1 = Match(user="Test", adoptable=adoptable1.id)
        match1.save()

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def test_match_model(self):
        match = Match.objects().first()
        print(match.user)
        print(match.adoptable.repository)
        assert match.user == "Test" and match.adoptable.repository == "testRepo"
