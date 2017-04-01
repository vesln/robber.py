import unittest
from robber import expect
from robber.matchers.length import Length, Empty, NotEmpty


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

    def test_register(self):
        expect(expect.matcher('empty')) == Empty


class TestNotEmpty(unittest.TestCase):
    def test_matches(self):
        expect(NotEmpty('').matches()).to.eq(False)
        expect(NotEmpty([]).matches()).to.eq(False)

        expect(NotEmpty('foo').matches()).to.eq(True)
        expect(NotEmpty([1, 2]).matches()).to.eq(True)

    def test_failure_message(self):
        not_empty = NotEmpty('foo')
        expect(not_empty.failure_message()) == 'Expected "foo" to be nonempty'

    def test_register(self):
        expect(expect.matcher('not_empty')) == NotEmpty
