from unittest import TestCase

from robber import expect
from tests import must_fail


class TestIdenticalIntegrations(TestCase):
    def test_equal_success(self):
        a_dict = {0: 1}

        expect(1).to.equal(1)
        expect('foo').to.equal('foo')
        expect(a_dict).to.equal(a_dict)

    @must_fail
    def test_equal_failure(self):
        expect({0: 1}).to.equal({0: 1})

    def test_not_equal_success(self):
        expect({0: 1}).not_to.equal({0: 1})

    @must_fail
    def test_not_equal_failure(self):
        a_dict = {0: 1}
        expect(a_dict).not_to.equal(a_dict)
