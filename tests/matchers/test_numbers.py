import unittest
from robber import expect, BadExpectation
from robber.matchers.numbers import Above, Below, Within, Change

class TestAbove(unittest.TestCase):
    def test_matches(self):
        expect(Above(2, 1).matches()) == True
        expect(Above(1, 2).matches()) == False

    def test_failure_message(self):
        above = Above(1, 2)
        expect(above.failure_message()) == 'Expected 1 to be above 2'

    def test_register(self):
        expect(expect.matcher('above')) == Above

class TestBelow(unittest.TestCase):
    def test_matches(self):
        expect(Below(1, 2).matches()) == True
        expect(Below(2, 1).matches()) == False

    def test_failure_message(self):
        below = Below(1, 2)
        expect(below.failure_message()) == 'Expected 1 to be below 2'

    def test_register(self):
        expect(expect.matcher('below')) == Below

class TestWithin(unittest.TestCase):
    def test_matches(self):
        expect(Within(1, 0, 2).matches()) == True
        expect(Within(2, 3, 4).matches()) == False

    def test_failure_message(self):
        within = Within(1, 2, 3)
        expect(within.failure_message()) == 'Expected 1 to be within 2 and 3'

    def test_register(self):
        expect(expect.matcher('within')) == Within

class TestChange(unittest.TestCase):
    def test_change_by_success(self):
        expect(Change(lambda x: x + 2, 1).by(2)) == True

    def test_change_by_raise_exception(self):
        def increase_by_2(x):
            return x + 2

        with self.assertRaises(BadExpectation) as cm:
            Change(increase_by_2, 1).by(1)
        self.assertEqual(cm.exception.message, 'Expect function increase_by_2 to change 1 by 1, but was changed by 2')
