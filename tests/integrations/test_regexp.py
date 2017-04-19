from unittest import TestCase

from robber import expect
from tests import must_fail


class TestRegexpIntegrations(TestCase):
    def test_match_success(self):
        expect('foo').to.match(r'foo')

    @must_fail
    def test_match_failure(self):
        expect('bar').to.match(r'foo')

    def test_not_match_success(self):
        expect('foo').not_to.match(r'bar$')

    @must_fail
    def test_not_match_failure(self):
        expect('foo').not_to.match(r'foo$')
