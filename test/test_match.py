import unittest
from collections import OrderedDict

from graphene.test import Client
from mongoengine import connect, disconnect

from lib.schema import schema

from lib.adoptable.model import Adoptable
from lib.match.model import Match


context = {
    "Authorization": "Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJSZXBvQWRvcHQiLCJleHAiOjE2MTc2OTg3MTEsImlhdCI6MTYxNzA5MzkxMSwiaXNzIjoiUmVwb0Fkb3B0IiwianRpIjoiYTQxYWJiNzEtZjY5MC00ZTg2LThkOTMtMjY2OWM2N2IxZTEwIiwibmJmIjoxNjE3MDkzOTExLCJ1c2VybmFtZSI6InRlc3QifQ.aN9ZLH1NV1Ag-6xgjoqzMes72zVA7u6V6kModYXvFdeUkaAWh1X9jib-1TzmpCfKFq025Ax9mNSAXlJnCXB5ctPD4w9QyCDGJMhdqpot0tMgt65JuVkkeCH-X1EB7OZDG2Wovc0D9h852RtbglVXkfmAcfVubIAPzA-z2Uk0-cLWb8hrVfrxG1ri4w3jWj6yw3s3qj5kbxaOqi6QNn_WjssPyAFlSvDfnfOLgN2WqZHKAmpFAC2fDdgPUFYQpWlgcfR-5wwvZfPBYE1J_zBSASaNTIRfuqCawxKCrfqn8Ek49eedYw6BZab7TVf760xrQ9Hz9_hah-Y2L--cMgdanA"
}


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
        print(match)
        print(match1)

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def test_match_model(self):
        match = Match.objects().first()
        assert match.user == "Test" and match.adoptable.repository == "testRepo"

    def test_my_matches(self):
        sent = """
                {
                  myMatches {
                    id
                    user
                    adoptable {
                      id
                      repository
                      owner
                    }
                  }
                }
                """

        expected = """test"""

        client = Client(schema)
        print(context)
        executed = client.execute(sent, context_value=context)
        print(executed)
        assert executed == expected
