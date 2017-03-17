import unittest
from robber import expect
from robber.matchers.length import Length, Empty, NotEmpty


class TestLength(unittest.TestCase):
    def test_matches(self):
        expect(Length('foo', 3).matches()) is True
        expect(Length([1, 2], 2).matches()) is True
        expect(Length({'test': 1}, 1).matches()) is True

        expect(Length('foo', 2).matches()) is False
        expect(Length([1, 2], 1).matches()) is False
        expect(Length({'test': 3}, 2).matches()) is False

    def test_failure_message(self):
        length = Length('foo', 2)
        expect(length.failure_message()) == 'Expected "foo" to have a length of 2'

    def test_register(self):
        expect(expect.matcher('length')) == Length


class TestEmpty(unittest.TestCase):
    def test_matches(self):
        expect(Empty('').matches()) is True
        expect(Empty([]).matches()) is True

        expect(Empty('foo').matches()) is False
        expect(Empty([1, 2]).matches()) is False

    def test_failure_message(self):
        empty = Empty('foo')
        expect(empty.failure_message()) == 'Expected "foo" to be empty'

    def test_register(self):
        expect(expect.matcher('empty')) == Empty


class TestNotEmpty(unittest.TestCase):
    def test_matches(self):
        expect(NotEmpty('').matches()) is False
        expect(NotEmpty([]).matches()) is False

        expect(NotEmpty('foo').matches()) is True
        expect(NotEmpty([1, 2]).matches()) is True

    def test_failure_message(self):
        not_empty = NotEmpty('foo')
        expect(not_empty.failure_message()) == 'Expected "foo" to be nonempty'

    def test_register(self):
        expect(expect.matcher('not_empty')) == NotEmpty
