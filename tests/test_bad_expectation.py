from unittest import TestCase

from robber import expect
from robber.bad_expectation import BadExpectation


class TestBadExpectation(TestCase):
    def test_message(self):
        # The error message will show up as long as it is the string representation of the Exception.
        # So this simple test is enough.
        message = 'You did something wrong!'
        bad_expectation = BadExpectation(message)
        expect(str(bad_expectation)).to.eq(message)
