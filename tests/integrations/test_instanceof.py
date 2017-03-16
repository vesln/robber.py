from unittest.case import TestCase

from robber import expect
from tests import must_fail


class TestInstanceIntegrations(TestCase):
    def test_instance(self):
        expect(expect(None)).to.be.instanceof(expect)

    @must_fail
    def test_instance(self):
        expect(expect(None)).to.be.instanceof(TestCase)
