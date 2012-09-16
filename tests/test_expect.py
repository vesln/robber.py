import unittest
from robber import expect, BadExpectation
from fixtures import TestMatcher
import matcher

# TODO: move to fixtures
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

    def test_to(self):
        expect(expect).to.have.chain('be')

    def test_a(self):
        expect(expect).to.have.chain('a')

    def test_an(self):
        expect(expect).to.have.chain('an')

    def test_be(self):
        expect(expect).to.have.chain('be')

    def test_have(self):
        expect(expect).to.have.chain('have')
