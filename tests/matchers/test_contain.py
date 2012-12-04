import unittest
from robber import expect
from robber.matchers.contain import Contain

class TestAbove(unittest.TestCase):
    def test_matches(self):
        expect(Contain({'key': 'value'}, 'key').matches()) == True
        expect(Contain([1, 2, 3], 2).matches()) == True
        expect(Contain((1, 2, 3), 3).matches()) == True

        expect(Contain({'key': 'value'}, 'other').matches()) == False
        expect(Contain([1, 2, 3], 4).matches()) == False
        expect(Contain((1, 2, 3), 4).matches()) == False

    def test_failure_message(self):
        contain = Contain([1, 2, 3], 4)
        expect(contain.failure_message()) == 'Expected {} to contain 4'.format([1, 2, 3])

    def test_register(self):
        expect(expect.matcher('contain')) == Contain
