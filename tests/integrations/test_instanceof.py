from unittest import TestCase

from robber import expect
from tests import must_fail


class TestInstanceIntegrations(TestCase):
    def test_instanceof_success(self):
        expect(expect(None)).to.be.instanceof(expect)

    @must_fail
    def test_instanceof_failure(self):
        expect(expect(None)).to.be.instanceof(TestCase)

    def test_not_to_be_instanceof_success(self):
        expect(expect(None)).not_to.be.instanceof(TestCase)

    @must_fail
    def test_not_to_be_instanceof_failure(self):
        expect(expect(None)).not_to.be.instanceof(expect)
