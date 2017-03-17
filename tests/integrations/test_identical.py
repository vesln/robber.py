from unittest import TestCase

from robber import expect
from tests import must_fail


class TestIdenticalIntegrations(TestCase):
    def test_equal_success(self):
        expect(1).to.equal(1)
        expect('foo').to.equal('foo')
        dict = {0: 1}
        expect(dict).to.equal(dict)

    @must_fail
    def test_equal_failure(self):
        expect({0: 1}).to.equal({0: 1})

    def test_not_equal_success(self):
        expect(1).to.not_equal(2)

    @must_fail
    def test_not_equal_failure(self):
        expect(1).to.not_equal(1)
