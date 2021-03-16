import unittest

from graphene.test import Client
from mongoengine import connect, disconnect
from lib.model.AdoptableModel import Adoptable
from lib.schema.AdoptableSchema import schema


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
        adoptable = Adoptable.objects().first()
        assert adoptable.repository == "testRepo"

    def test_get_all_adoptables(self):
        sent = '''
        {
          allAdoptables {
            repository
          }
        }
        '''

        expected = {'data': {'allAdoptables': [{'repository': 'testRepo1'}, {'repository': 'testRepo'}]}}

        client = Client(schema)
        executed = client.execute(sent)
        assert executed == expected

    def test_get_pagination_adoptables_first_page(self):
        sent = '''
                {
                  paginationAdoptables(page: 0 limit: 1) {
                    repository
                  }
                }
                '''

        expected = {'data': {'paginationAdoptables': [{'repository': 'testRepo1'}]}}

        client = Client(schema)
        executed = client.execute(sent)
        assert executed == expected

    def test_get_pagination_adoptables_second_page(self):
        sent = '''
                {
                  paginationAdoptables(page: 1 limit: 1) {
                    repository
                  }
                }
                '''

        expected = {'data': {'paginationAdoptables': [{'repository': 'testRepo'}]}}

        client = Client(schema)
        executed = client.execute(sent)
        assert executed == expected

    def test_get_pagination_adoptables_multiple_items_per_page(self):
        sent = '''
                {
                  paginationAdoptables(page: 0 limit: 10) {
                    repository
                  }
                }
                '''

        expected = {'data': {'paginationAdoptables': [{'repository': 'testRepo1'}, {'repository': 'testRepo'}]}}

        client = Client(schema)
        executed = client.execute(sent)
        assert executed == expected

    def test_get_pagination_adoptables_no_adoptables_in_page(self):
        sent = '''
                {
                  paginationAdoptables(page: 1 limit: 10) {
                    repository
                  }
                }
                '''

        expected = {'data': {'paginationAdoptables': []}}

        client = Client(schema)
        executed = client.execute(sent)
        assert executed == expected