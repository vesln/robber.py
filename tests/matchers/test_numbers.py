import unittest
from robber import expect, BadExpectation
from robber.matchers.numbers import Above, Below, Within, Change


class TestAbove(unittest.TestCase):
    def test_matches(self):
        expect(Above(2, 1).matches()).to.eq(True)
        expect(Above(1, 2).matches()).to.eq(False)

    def test_failure_message(self):
        above = Above(1, 2)
        message = above.explanation.message
        expect(message) == """
A = 1
B = 2
Expected A to be above B
"""

    def test_negative_failure_message(self):
        above = Above(2, 1, is_negative=True)
        message = above.explanation.message
        expect(message) == """
A = 2
B = 1
Expected A not to be above B
"""

    def test_register(self):
        expect(expect.matcher('above')) == Above


class TestBelow(unittest.TestCase):
    def test_matches(self):
        expect(Below(1, 2).matches()).to.eq(True)
        expect(Below(2, 1).matches()).to.eq(False)

    def test_failure_message(self):
        below = Below(2, 1)
        message = below.explanation.message
        expect(message) == """
A = 2
B = 1
Expected A to be below B
"""

    def test_negative_failure_message(self):
        below = Below(1, 2, is_negative=True)
        message = below.explanation.message
        expect(message) == """
A = 1
B = 2
Expected A not to be below B
"""

    def test_register(self):
        expect(expect.matcher('below')) == Below


class TestWithin(unittest.TestCase):
    def test_matches(self):
        expect(Within(1, 0, False, 2).matches()).to.eq(True)
        expect(Within(2, 3, False, 4).matches()).to.eq(False)

    def test_failure_message(self):
        within = Within(1, 2, False, 3)
        message = within.explanation.message
        expect(message) == """
A = 1
B = 2
C = 3
Expected A to be within B and C
"""

    def test_negative_failure_message(self):
        within = Within(1, 0, True, 2)
        message = within.explanation.message
        expect(message) == """
A = 1
B = 0
C = 2
Expected A not to be within B and C
"""

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
            expect(exception.message) == """
A = increase_by_2
B = 1
C = 1
Z = 2
Expected A to change B by C
Actually changed by Z
"""

    def test_change_by_raise_exception_with_not_to(self):
        def increase_by_2(x):
            return x + 2

        try:
            Change(increase_by_2, 1, is_negative=True).by(2)
        except BadExpectation as exception:
            expect(exception.message) == """
A = increase_by_2
B = 1
C = 2
Expected A not to change B by C
But it happened
"""

    def test_register(self):
        expect(expect.matcher('change')) == Change
