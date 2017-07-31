import unittest

from robber import expect, BadExpectation
from robber.matchers.base import Base
from tests.fixtures import TestWillMatch, TestWontMatch


class TestBase(unittest.TestCase):
    def test_it_stores_actual_and_expected(self):
        base = Base('actual', 'expected')

        expect(base.actual) == 'actual'
        expect(base.expected) == 'expected'

    def test_it_calls_matches(self):
        matcher = TestWillMatch('actual', 'expected')
        matcher.match()
        expect(matcher.called).to.be.true()

    def test_it_raises_an_execption_when_cant_match(self):
        matcher = TestWontMatch('actual', 'expected')

        try:
            matcher.match()
        except BadExpectation as failure:
            expect(failure.message).to.eq('Failure message')
        else:
            raise BadExpectation('it should raise an exception')

    def test_negative_message(self):
        negated_base = Base(actual='actual', expected='expected', is_negative=True)
        positive_base = Base(actual='actual', expected='expected', is_negative=False)

        expect(negated_base.negative_message).to.eq(' not')
        expect(positive_base.negative_message).to.eq('')

    def test_match(self):
        matcher = TestWillMatch('actual', 'expected')
        expect(matcher.match()).to.eq(True)
