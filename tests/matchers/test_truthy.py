import unittest
from robber import expect
from robber.matchers.truthy import Truthy, Falsy


class TestTruthy(unittest.TestCase):
    def test_matches(self):
        expect(Truthy(expect).matches()) == True
        expect(Truthy(['foo']).matches()) == True

        expect(Truthy(None).matches()) == False
        expect(Truthy([]).matches()) == False

    def test_failure_message(self):
        truthy = Truthy(False)
        expect(truthy.failure_message()) == 'Expected "False" to be truthy'

    def test_register(self):
        expect(expect.matcher('truthy')) == Truthy


class TestFalsy(unittest.TestCase):
    def test_matches(self):
        expect(Falsy(None).matches()) == True
        expect(Falsy([]).matches()) == True

        expect(Falsy(expect).matches()) == False
        expect(Falsy(['foo']).matches()) == False

    def test_failure_message(self):
        falsy = Falsy(True)
        expect(falsy.failure_message()) == 'Expected "True" to be falsy'

    def test_register(self):
        expect(expect.matcher('falsy')) == Falsy
