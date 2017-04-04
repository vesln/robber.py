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
        expect(length.failure_message()) == 'Expected "foo" to have a length of 2'

    def test_failure_message_with_not_to(self):
        length = Length('foo', 3, is_negative=True)
        expect(length.failure_message()) == 'Expected "foo" not to have a length of 3'

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
        expect(empty.failure_message()) == 'Expected "foo" to be empty'

    def test_failure_message_with_not_to(self):
        empty = Empty('', is_negative=True)
        expect(empty.failure_message()) == 'Expected "" not to be empty'

    def test_register(self):
        expect(expect.matcher('empty')) == Empty
