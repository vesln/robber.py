import unittest

from robber import expect
from robber.matchers.truthy import Truthy


class TestTruthy(unittest.TestCase):
    def test_matches(self):
        expect(Truthy(expect).matches()).to.eq(True)
        expect(Truthy(['foo']).matches()).to.eq(True)

        expect(Truthy(None).matches()).to.eq(False)
        expect(Truthy([]).matches()).to.eq(False)

    def test_failure_message(self):
        truthy = Truthy(False)
        expect(truthy.failure_message()) == 'Expected "False" to be truthy'

    def test_negative_failure_message(self):
        truthy = Truthy(True, is_negative=True)
        expect(truthy.failure_message()) == 'Expected "True" to be falsy'

    def test_register(self):
        expect(expect.matcher('truthy')) == Truthy
        expect(expect.matcher('falsy')) == Truthy
