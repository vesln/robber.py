import unittest
from robber import expect
from robber.matchers.contain import Contain, NotContain


class TestContain(unittest.TestCase):
    def test_matches(self):
        expect(Contain({'key': 'value'}, 'key').matches()) is True
        expect(Contain([1, 2, 3], 2).matches()) is True
        expect(Contain((1, 2, 3), 3).matches()) is True

        expect(Contain({'key': 'value'}, 'other').matches()) is False
        expect(Contain([1, 2, 3], 4).matches()) is False
        expect(Contain((1, 2, 3), 4).matches()) is False

    def test_failure_message(self):
        contain = Contain([1, 2, 3], 4)
        expect(contain.failure_message()) == 'Expected {0} to contain 4'.format([1, 2, 3])

    def test_register(self):
        expect(expect.matcher('contain')) == Contain


class TestNotContain(unittest.TestCase):
    def test_matches(self):
        expect(NotContain({'key': 'value'}, 'other').matches()) is True
        expect(NotContain([1, 2, 3], 4).matches()) is True
        expect(NotContain((1, 2, 3), 4).matches()) is True

        expect(NotContain({'key': 'value'}, 'key').matches()) is False
        expect(NotContain([1, 2, 3], 2).matches()) is False
        expect(NotContain((1, 2, 3), 3).matches()) is False

    def test_failure_message(self):
        not_contain = NotContain([1, 2, 3], 3)
        expect(not_contain.failure_message()) == 'Expected {0} to not contain 3'.format([1, 2, 3])

    def test_register(self):
        expect(expect.matcher('not_contain')) == NotContain
