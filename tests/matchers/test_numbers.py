import unittest
from robber import expect
from robber.matchers.numbers import Above, Below, Within


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
        expect(Within(1, 0, False, 2).matches()) == True
        expect(Within(2, 3, False, 4).matches()) == False

    def test_failure_message(self):
        within = Within(1, 2, False, 3)
        expect(within.failure_message()) == 'Expected 1 to be within 2 and 3'

    def test_register(self):
        expect(expect.matcher('within')) == Within
