from unittest import TestCase

from robber import expect
from tests import must_fail


class TestCallableIntegrations(TestCase):
    def test_callable_success(self):
        def a():
            pass
        expect(a).to.be.callable()

    @must_fail
    def test_callable_failure(self):
        expect('a').to.be.callable()
        expect(1).to.be.callable()

    def test_not_to_be_callable_success(self):
        expect('a').not_to.be.callable()
        expect(1).not_to.be.callable()

    @must_fail
    def test_not_to_be_callable_failure(self):
        def a():
            pass
        expect(a).not_to.be.callable()
