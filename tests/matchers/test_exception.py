import unittest

from robber import expect
from robber.matchers.exception import ExceptionMatcher


class TestExceptionMatcher(unittest.TestCase):
    def raise_exception(self, ex):
        raise ex

    def test_matches(self):
        expect(ExceptionMatcher(lambda: 1 / 0, ZeroDivisionError).matches()).to.eq(True)
        expect(ExceptionMatcher(lambda: None, Exception).matches()).to.eq(False)

    def test_actual_is_not_callable(self):
        self.assertRaises(TypeError, ExceptionMatcher(None, Exception).matches)

    def test_failure_message_with_wrong_exception(self):
        exception_raised = ExceptionMatcher(lambda: self.raise_exception(TypeError()), ZeroDivisionError)
        message = exception_raised.explanation.message
        expect(message) == """
A = 'ZeroDivisionError'
C = 'TypeError'
Expected A to be raised
Actually got C
"""

    def test_negative_failure_message_with_wrong_exception(self):
        exception_raised = ExceptionMatcher(
            lambda: self.raise_exception(ZeroDivisionError()), ZeroDivisionError, is_negative=True)
        message = exception_raised.explanation.message
        expect(message) == """
A = 'ZeroDivisionError'
C = 'ZeroDivisionError'
Expected A not to be raised
Actually got C
"""

    def test_failure_message_with_no_exception_was_raised(self):
        no_exception = ExceptionMatcher(lambda: None, Exception)
        message = no_exception.explanation.message
        expect(message) == """
A = 'Exception'
C = 'nothing'
Expected A to be raised
Actually got C
"""
