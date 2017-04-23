import unittest

from robber import expect
from robber.matchers.length import Length, Empty


class TestLength(unittest.TestCase):
    def test_matches(self):
        expect(Length('foo', 3).matches()).to.eq(True)
        expect(Length([1, 2], 2).matches()).to.eq(True)
        expect(Length({'test': 1}, 1).matches()).to.eq(True)

        expect(Length('foo', 2).matches()).to.eq(False)
        expect(Length([1, 2], 1).matches()).to.eq(False)
        expect(Length({'test': 3}, 2).matches()).to.eq(False)

    def test_failure_message(self):
        length = Length('foo', 2)
        message = length.explanation.message
        expect(message) == """
A = 'foo'
B = 2
Expected A to have length of B
"""

    def test_negative_failure_message(self):
        length = Length('foo', 3, is_negative=True)
        message = length.explanation.message
        expect(message) == """
A = 'foo'
B = 3
Expected A not to have length of B
"""

    def test_register(self):
        expect(expect.matcher('length')) == Length


class TestEmpty(unittest.TestCase):
    def test_matches(self):
        expect(Empty('').matches()).to.eq(True)
        expect(Empty([]).matches()).to.eq(True)

        expect(Empty('foo').matches()).to.eq(False)
        expect(Empty([1, 2]).matches()).to.eq(False)

    def test_failure_message(self):
        empty = Empty('foo')
        expect(empty.explanation.message) == """
A = 'foo'
Expected A to be empty
"""

    def test_negative_failure_message(self):
        empty = Empty('', is_negative=True)
        expect(empty.explanation.message) == """
A = ''
Expected A not to be empty
"""

    def test_register(self):
        expect(expect.matcher('empty')) == Empty
