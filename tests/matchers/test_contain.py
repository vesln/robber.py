import unittest
from robber import expect
from robber.matchers.contain import Contain, Exclude


class TestContain(unittest.TestCase):
    def test_matches(self):
        expect(Contain({'key': 'value'}, 'key').matches()).to.eq(True)
        expect(Contain([1, 2, 3], 2).matches()).to.eq(True)
        expect(Contain((1, 2, 3), 3).matches()).to.eq(True)

        expect(Contain({'key': 'value'}, 'other').matches()).to.eq(False)
        expect(Contain([1, 2, 3], 4).matches()).to.eq(False)
        expect(Contain((1, 2, 3), 4).matches()).to.eq(False)

    def test_failure_message(self):
        contain = Contain([1, 2, 3], 4)
        expect(contain.failure_message()) == 'Expected {0} to contain 4'.format([1, 2, 3])

    def test_negative_failure_message(self):
        contain = Contain([1, 2, 3], 2, is_negative=True)
        expect(contain.failure_message()) == 'Expected {0} not to contain 2'.format([1, 2, 3])

    def test_register(self):
        expect(expect.matcher('contain')) == Contain


class TestNotContain(unittest.TestCase):
    def test_matches(self):
        expect(Exclude({'key': 'value'}, 'other').matches()).to.eq(True)
        expect(Exclude([1, 2, 3], 4).matches()).to.eq(True)
        expect(Exclude((1, 2, 3), 4).matches()).to.eq(True)

        expect(Exclude({'key': 'value'}, 'key').matches()).to.eq(False)
        expect(Exclude([1, 2, 3], 2).matches()).to.eq(False)
        expect(Exclude((1, 2, 3), 3).matches()).to.eq(False)

    def test_failure_message(self):
        not_contain = Exclude([1, 2, 3], 3)
        expect(not_contain.failure_message()) == 'Expected {0} to exclude 3'.format([1, 2, 3])

    def test_register(self):
        expect(expect.matcher('exclude')) == Exclude
