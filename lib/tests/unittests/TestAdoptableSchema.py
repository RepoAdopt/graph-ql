import unittest

from main import app
from graphene.test import Client
from mongoengine import connect, disconnect
from lib.model.AdoptableModel import Adoptable
from lib.schema.AdoptableSchema import schema

app.testing = True


class TestAdoptable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('RepoAdoptTest', host='mongomock://localhost/')
        adoptable = Adoptable(repository="testRepo")
        adoptable.save()
        adoptable1 = Adoptable(repository="testRepo1")
        adoptable1.save()

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def test_adoptable_model(self):
        fresh_adoptable = Adoptable.objects().first()
        assert fresh_adoptable.repository == "testRepo"

    def test_get_adoptables(self):
        sent = '''
        {
          allAdoptables {
            edges{
              node{
                repository
              }
            }
          }
        }
        '''

        expected = {'data': {'allAdoptables': {'edges': [{'node': {'repository': 'testRepo'}}, {'node': {'repository': 'testRepo1'}}]}}}

        client = Client(schema)
        executed = client.execute(sent)
        print(executed)
        assert executed == expected
