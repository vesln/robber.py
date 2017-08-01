import unittest

from robber import expect
from tests import TestMatcher
from tests.util import must_fail


class TestExpectation(unittest.TestCase):
    def test_register_a_matcher(self):
        expect.register('test_matcher', TestMatcher)
        expect('test').test_matcher('bar')

    def test_registered_a_matcher(self):
        expect.register('test_matcher', TestMatcher)
        expect(expect.registered('test_matcher')).to.eq(True)
        expect(expect.registered('not_registered')).to.eq(False)

    def test_unregisted_a_matcher(self):
        expect.register('test_matcher', TestMatcher)
        expect.unregister('test_matcher')
        expect(expect.registered('test_matcher')).to.eq(False)

    def test_it_can_return_matcher(self):
        expect.register('test_matcher', TestMatcher)
        matcher = expect.matcher('test_matcher')
        expect(matcher) == TestMatcher

    def test_to(self):
        expect(expect).to.have.chain('to')

    def test_a(self):
        expect(expect).to.have.chain('a')

    def test_an(self):
        expect(expect).to.have.chain('an')

    def test_be(self):
        expect(expect).to.have.chain('be')

    def test_have(self):
        expect(expect).to.have.chain('have')

    def test_chaining(self):
        expectation = expect(object)
        expect(expectation.to).to.equal(expectation.to.be)

    def test_multiple_not_to_success(self):
        expect(1).eq(1)
        expect(1).not_to.not_to.eq(1)
        expect(1).not_to.not_to.not_to.not_to.eq(1)

        expect(1).to.ne(2)
        expect(1).not_to.not_to.ne(2)
        expect(1).not_to.not_to.not_to.not_to.ne(2)

    @must_fail
    def test_multiple_not_to_failure(self):
        expect(1).not_to.eq(1)
        expect(1).not_to.not_to.not_to.eq(1)
        expect(1).not_to.not_to.not_to.not_to.not_to.eq(1)

        expect(1).not_to.ne(2)
        expect(1).not_to.not_to.not_to.ne(2)
        expect(1).not_to.not_to.not_to.not_to.not_to.ne(2)
