import unittest
from robber import expect, BadExpectation
from robber.matchers.numbers import Above, Below, Within, Change


class TestAbove(unittest.TestCase):
    def test_matches(self):
        expect(Above(2, 1).matches()).to.eq(True)
        expect(Above(1, 2).matches()).to.eq(False)

    def test_failure_message(self):
        above = Above(1, 2)
        expect(above.failure_message()) == 'Expected 1 to be above 2'

    def test_negative_failure_message(self):
        above = Above(2, 1, is_negative=True)
        expect(above.failure_message()) == 'Expected 2 not to be above 1'

    def test_register(self):
        expect(expect.matcher('above')) == Above


class TestBelow(unittest.TestCase):
    def test_matches(self):
        expect(Below(1, 2).matches()).to.eq(True)
        expect(Below(2, 1).matches()).to.eq(False)

    def test_failure_message(self):
        below = Below(2, 1)
        expect(below.failure_message()) == 'Expected 2 to be below 1'

    def test_negative_failure_message(self):
        below = Below(1, 2, is_negative=True)
        expect(below.failure_message()) == 'Expected 1 not to be below 2'

    def test_register(self):
        expect(expect.matcher('below')) == Below


class TestWithin(unittest.TestCase):
    def test_matches(self):
        expect(Within(1, 0, False, 2).matches()).to.eq(True)
        expect(Within(2, 3, False, 4).matches()).to.eq(False)

    def test_failure_message(self):
        within = Within(1, 2, False, 3)
        expect(within.failure_message()) == 'Expected 1 to be within 2 and 3'

    def test_negative_failure_message(self):
        within = Within(1, 0, True, 2)
        expect(within.failure_message()) == 'Expected 1 not to be within 0 and 2'

    def test_register(self):
        expect(expect.matcher('within')) == Within


class TestChange(unittest.TestCase):
    def test_change_by_success(self):
        expect(Change(lambda x: x + 2, 1).by(2)).to.eq(True)

    def test_change_by_raise_exception(self):
        def increase_by_2(x):
            return x + 2

        try:
            Change(increase_by_2, 1).by(1)
        except BadExpectation as exception:
            expect(exception.message) == 'Expected function increase_by_2 to change 1 by 1, but was changed by 2'

    def test_change_by_raise_exception_with_not_to(self):
        def increase_by_2(x):
            return x + 2

        try:
            Change(increase_by_2, 1, is_negative=True).by(2)
        except BadExpectation as exception:
            expect(exception.message) == 'Expected function increase_by_2 not to change 1 by 2, but was changed by 2'

    def test_register(self):
        expect(expect.matcher('change')) == Change
