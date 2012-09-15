import unittest

from expect.base import expect
from expect.base import Expectation
from expect.base import BadExpectation

class TestExpect(unittest.TestCase):
    def test_expect_returns_a_new_expectation(self):
        expected = isinstance(expect('test'), Expectation)
        assert(expected)

class TestExpectation(unittest.TestCase):
    def test_to_returns_self(self):
        expectation = Expectation(None)
        assert(expectation == expectation.to)

    def test_equal(self):
        expect('test').to.equal('test')
        expect({1: 1}).to.equal({1:1})

        try:
            expect('test').to.equal('spec')
        except BadExpectation as error:
            assert(error.message == 'Expected "test" to equal "spec"')
        else:
            raise BadExpectation('test should not equal foo')

    def test_not_equal(self):
        expect('test').to.not_equal('spec')

        try:
            expect('test').to.not_equal('test')
        except BadExpectation as error:
            assert(error.message == 'Expected "test" to not equal "test"')
        else:
            raise BadExpectation('test should equal test')

    def test_be(self):
        expect(1).to.be(1)

        try:
            first  = {0: 1}
            second = {0: 1}

            expect(first).to.be(second)
        except BadExpectation as error:
            expect(error.message).to.equal('Expected "{0: 1}" to be "{0: 1}"')
        else:
            raise BadExpectation('test should not equal foo')
