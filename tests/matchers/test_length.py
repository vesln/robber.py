import unittest
from robber import expect
from robber.matchers.length import Length, Empty

class TestLength(unittest.TestCase):
    def test_matches(self):
        expect(Length('foo', 3).matches()) == True
        expect(Length([1, 2], 2).matches()) == True
        expect(Length({'test': 1}, 1).matches()) == True

        expect(Length('foo', 2).matches()) == False
        expect(Length([1, 2], 1).matches()) == False
        expect(Length({'test': 3}, 2).matches()) == False

    def test_failure_message(self):
        length = Length('foo', 2)
        expect(length.failure_message()) == 'Expected "foo" to have a length of 2'

    def test_register(self):
        expect(expect.matcher('length')) == Length

class TestEmpty(unittest.TestCase):
    def test_matches(self):
        expect(Empty('').matches()) == True
        expect(Empty([]).matches()) == True

        expect(Empty('foo').matches()) == False
        expect(Empty([1, 2]).matches()) == False

    def test_failure_message(self):
        empty = Empty('foo')
        expect(empty.failure_message()) == 'Expected "foo" to be empty'

    def test_register(self):
        expect(expect.matcher('empty')) == Empty
