import unittest
from robber import expect
from robber.matchers.truthy import Truthy, Falsy


class TestTruthy(unittest.TestCase):
    def test_matches(self):
        expect(Truthy(expect).matches()) is True
        expect(Truthy(['foo']).matches()) is True

        expect(Truthy(None).matches()) is False
        expect(Truthy([]).matches()) is False

    def test_failure_message(self):
        truthy = Truthy(False)
        expect(truthy.failure_message()) == 'Expected "False" to be truthy'

    def test_register(self):
        expect(expect.matcher('truthy')) == Truthy


class TestFalsy(unittest.TestCase):
    def test_matches(self):
        expect(Falsy(None).matches()) is True
        expect(Falsy([]).matches()) is True

        expect(Falsy(expect).matches()) is False
        expect(Falsy(['foo']).matches()) is False

    def test_failure_message(self):
        falsy = Falsy(True)
        expect(falsy.failure_message()) == 'Expected "True" to be falsy'

    def test_register(self):
        expect(expect.matcher('falsy')) == Falsy
