import unittest
from robber import expect
from robber.matchers.truthy import Truthy, Falsy


class TestTruthy(unittest.TestCase):
    def test_matches(self):
        expect(Truthy(expect).matches()).to.eq(True)
        expect(Truthy(['foo']).matches()).to.eq(True)

        expect(Truthy(None).matches()).to.eq(False)
        expect(Truthy([]).matches()).to.eq(False)

    def test_failure_message(self):
        truthy = Truthy(False)
        expect(truthy.failure_message()) == 'Expected "False" to be truthy'

    def test_failure_message_with_not_to(self):
        truthy = Truthy(True, is_negative=True)
        expect(truthy.failure_message()) == 'Expected "True" not to be truthy'

    def test_register(self):
        expect(expect.matcher('truthy')) == Truthy


class TestFalsy(unittest.TestCase):
    def test_matches(self):
        expect(Falsy(None).matches()).to.eq(True)
        expect(Falsy([]).matches()).to.eq(True)

        expect(Falsy(expect).matches()).to.eq(False)
        expect(Falsy(['foo']).matches()).to.eq(False)

    def test_failure_message(self):
        falsy = Falsy(True)
        expect(falsy.failure_message()) == 'Expected "True" to be falsy'

    def test_failure_message_with_not_to(self):
        falsy = Falsy(False, is_negative=True)
        expect(falsy.failure_message()) == 'Expected "False" not to be falsy'

    def test_register(self):
        expect(expect.matcher('falsy')) == Falsy
