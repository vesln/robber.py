import unittest

from robber.base import expect
from robber.base import BadExpectation

class TestMatcher:
    def __init__(self, actual, expected):
        expect(actual) == 'test'
        expect(expected) == 'bar'

class TestExpectation(unittest.TestCase):
    def test_register_a_matcher(self):
        expect.register('test_matcher', TestMatcher)
        test_matcher = expect('test').test_matcher('bar')
        assert(isinstance(test_matcher, TestMatcher))

    def test_registered_a_matcher(self):
        expect.register('test_matcher', TestMatcher)
        expect(expect.registered('test_matcher')) == True
        expect(expect.registered('not_registered')) == False

    def test_unregisted_a_matcher(self):
        expect.register('test_matcher', TestMatcher)
        expect.unregister('test_matcher')
        expect(expect.registered('test_matcher')) == False

    def test_to_returns_self(self):
        expectation = expect(None)
        expect(expectation).to.equal(expectation.to)

    def test_be_returns_self(self):
        expectation = expect(None)
        expect(expectation).to.equal(expectation.be)

    def test_eq(self):
        expect('test').to.eq('test')

        try:
            expect('test').to.eq('spec')
        except BadExpectation as error:
            assert(error.message == 'Expected "test" to equal "spec"')
        else:
            raise BadExpectation('test should not equal foo')

    def test_not_eq(self):
        expect('test').to.not_eq('spec')

        try:
            expect('test').to.not_eq('test')
        except BadExpectation as error:
            assert(error.message == 'Expected "test" to not equal "test"')
        else:
            raise BadExpectation('test should equal test')

    def test_ne(self):
        expect('test').to.ne('spec')

        try:
            expect('test').to.ne('test')
        except BadExpectation as error:
            assert(error.message == 'Expected "test" to not equal "test"')
        else:
            raise BadExpectation('test should equal test')

    def test_comparison_eq(self):
        expect('test') == ('test')

        try:
            expect('test') == 'spec'
        except BadExpectation as error:
            assert(error.message == 'Expected "test" to equal "spec"')
        else:
            raise BadExpectation('test should not equal foo')

    def test_comparison_ne(self):
        expect('test') != ('spec')

        try:
            expect('test') != 'test'
        except BadExpectation as error:
            assert(error.message == 'Expected "test" to not equal "test"')
        else:
            raise BadExpectation('test should equal test')

    def test_equal(self):
        expect(1).to.equal(1)

        try:
            expect({0: 1}).to.equal({0: 1})
        except BadExpectation as error:
            expect(error.message).to.eq('Expected "{0: 1}" to be "{0: 1}"')
        else:
            raise BadExpectation('test should not equal foo')

    def test_not_equal(self):
        expect({0: 1}).to.not_equal({0: 1})

        try:
            expect(1).to.not_equal(1)
        except BadExpectation as error:
            expect(error.message).to.not_equal('Expected "1" to not be "1"')
        else:
            raise BadExpectation('1 should be 1')
