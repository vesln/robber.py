import unittest
from robber import expect, BadExpectation
from robber.matchers.base import Base

# TODO: use stubs

class TestMatcher(Base):
    called = False

    def matches(self):
        self.called = True
        return True

class TestNotMatcher(Base):
    def matches(self):
        return False

    def failure_message(self):
        return 'Failure message'

class TestBase(unittest.TestCase):
    def test_it_stores_actual_and_expected(self):
        base = Base('actual', 'expected')

        expect(base.actual) == 'actual'
        expect(base.expected) == 'expected'

    def test_it_calls_matches(self):
        matcher = TestMatcher('actual', 'expected')
        matcher.match()
        expect(matcher.called).to.be.true()

    def test_it_raises_an_execption_when_cant_match(self):
        matcher = TestNotMatcher('actual', 'expected')

        try:
            matcher.match()
        except BadExpectation as failure:
            expect(failure.message).to.eq('Failure message')
        else:
            raise BadExpectation, 'it should raise an exception'
