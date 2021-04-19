import unittest

from flask import request
from graphene.test import Client
from mongoengine import connect, disconnect

from lib.schema import schema

from lib.adoptable.model import Adoptable


class TestAdoptable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connect("RepoAdoptTest", host="mongomock://localhost/")

        adoptable = Adoptable(repository="testRepo", owner="Test")
        adoptable.save()
        adoptable1 = Adoptable(repository="testRepo1", owner="Test")
        adoptable1.save()

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def test_adoptable_model(self):
        adoptable = Adoptable.objects().first()
        assert adoptable.repository == "testRepo"

    def test_get_pagination_adoptables_first_page(self):
        sent = """
                {
                  adoptable(page: 0 limit: 1) {
                    repository
                  }
                }
                """

        expected = {"data": {"adoptable": [{"repository": "testRepo1"}]}}

        client = Client(schema)
        executed = client.execute(sent)
        print(executed)
        assert executed == expected

    def test_get_pagination_adoptables_second_page(self):
        sent = """
                {
                  adoptable(page: 1 limit: 1) {
                    repository
                  }
                }
                """

        expected = {"data": {"adoptable": [{"repository": "testRepo"}]}}

        client = Client(schema)
        executed = client.execute(sent)
        assert executed == expected

    def test_get_pagination_adoptables_multiple_items_per_page(self):
        sent = """
                {
                  adoptable(page: 0 limit: 10) {
                    repository
                  }
                }
                """

        expected = {
            "data": {
                "adoptable": [{"repository": "testRepo1"}, {"repository": "testRepo"}]
            }
        }

        client = Client(schema)
        executed = client.execute(sent)
        assert executed == expected

    def test_get_pagination_adoptables_no_adoptables_in_page(self):
        sent = """
                {
                  adoptable(page: 1 limit: 10) {
                    repository
                  }
                }
                """

        expected = {"data": {"adoptable": []}}

        client = Client(schema)
        executed = client.execute(sent)
        assert executed == expected

    # TODO Fix this when you can pass extra arguments
    # def test_create_adoptable(self):
    #     sent = """mutation {
    #               createAdoptable(repository: "test",description: "my desc") {
    #                 adoptable {
    #                   description
    #                   repository
    #                 }
    #               }
    #             }"""
    #
    #     expected = {
    #         "data": {
    #             "createAdoptable": {
    #                 "adoptable": {"description": "my desc", "repository": "test"}
    #             }
    #         }
    #     }
    #
    #     client = Client(schema)
    #     request.headers = {
    #         "Authorization": "Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJSZXBvQWRvcHQiLCJleHAiOjE2MTc2OTg3MTEsImlhdCI6MTYxNzA5MzkxMSwiaXNzIjoiUmVwb0Fkb3B0IiwianRpIjoiYTQxYWJiNzEtZjY5MC00ZTg2LThkOTMtMjY2OWM2N2IxZTEwIiwibmJmIjoxNjE3MDkzOTExLCJ1c2VybmFtZSI6InRlc3QifQ.aN9ZLH1NV1Ag-6xgjoqzMes72zVA7u6V6kModYXvFdeUkaAWh1X9jib-1TzmpCfKFq025Ax9mNSAXlJnCXB5ctPD4w9QyCDGJMhdqpot0tMgt65JuVkkeCH-X1EB7OZDG2Wovc0D9h852RtbglVXkfmAcfVubIAPzA-z2Uk0-cLWb8hrVfrxG1ri4w3jWj6yw3s3qj5kbxaOqi6QNn_WjssPyAFlSvDfnfOLgN2WqZHKAmpFAC2fDdgPUFYQpWlgcfR-5wwvZfPBYE1J_zBSASaNTIRfuqCawxKCrfqn8Ek49eedYw6BZab7TVf760xrQ9Hz9_hah-Y2L--cMgdanA"
    #     }
    #     context = object()
    #     context.token = {
    #         "Authorization": "Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJSZXBvQWRvcHQiLCJleHAiOjE2MTc2OTg3MTEsImlhdCI6MTYxNzA5MzkxMSwiaXNzIjoiUmVwb0Fkb3B0IiwianRpIjoiYTQxYWJiNzEtZjY5MC00ZTg2LThkOTMtMjY2OWM2N2IxZTEwIiwibmJmIjoxNjE3MDkzOTExLCJ1c2VybmFtZSI6InRlc3QifQ.aN9ZLH1NV1Ag-6xgjoqzMes72zVA7u6V6kModYXvFdeUkaAWh1X9jib-1TzmpCfKFq025Ax9mNSAXlJnCXB5ctPD4w9QyCDGJMhdqpot0tMgt65JuVkkeCH-X1EB7OZDG2Wovc0D9h852RtbglVXkfmAcfVubIAPzA-z2Uk0-cLWb8hrVfrxG1ri4w3jWj6yw3s3qj5kbxaOqi6QNn_WjssPyAFlSvDfnfOLgN2WqZHKAmpFAC2fDdgPUFYQpWlgcfR-5wwvZfPBYE1J_zBSASaNTIRfuqCawxKCrfqn8Ek49eedYw6BZab7TVf760xrQ9Hz9_hah-Y2L--cMgdanA"
    #     }
    #
    #     executed = client.execute(sent, context=context)
    #     print(executed)
    #     assert executed == expected
    #
    #     Adoptable.objects(repository="test").delete()
