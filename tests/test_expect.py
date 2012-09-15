import unittest
from robber import expect, BadExpectation

class TestMatcher:
    def __init__(self, actual, expected):
        expect(actual) == 'test'
        expect(expected) == 'bar'

    def match(self):
        return True

class TestExpectation(unittest.TestCase):
    def test_register_a_matcher(self):
        expect.register('test_matcher', TestMatcher)
        test_matcher = expect('test').test_matcher('bar')

    def test_registered_a_matcher(self):
        expect.register('test_matcher', TestMatcher)
        expect(expect.registered('test_matcher')) == True
        expect(expect.registered('not_registered')) == False

    def test_unregisted_a_matcher(self):
        expect.register('test_matcher', TestMatcher)
        expect.unregister('test_matcher')
        expect(expect.registered('test_matcher')) == False

    def test_it_can_return_matcher(self):
        expect.register('test_matcher', TestMatcher)
        matcher = expect.matcher('test_matcher')
        expect(matcher) == TestMatcher

    def test_to_returns_self(self):
        expectation = expect(None)
        expect(expectation).to.equal(expectation.to)

    def test_a_returns_self(self):
        expectation = expect(None)
        expect(expectation).to.equal(expectation.a)

    def test_an_returns_self(self):
        expectation = expect(None)
        expect(expectation).to.equal(expectation.an)

    def test_be_returns_self(self):
        expectation = expect(None)
        expect(expectation).to.equal(expectation.be)
