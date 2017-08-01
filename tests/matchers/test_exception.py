from unittest import TestCase

from robber import expect
from robber.matchers.exception import ExceptionMatcher, ExactExceptionMatcher


class TestExceptionMatcher(TestCase):
    def raise_exception(self, ex):
        raise ex

    def test_verb(self):
        exception = ExceptionMatcher(lambda: 1 / 1)
        expect(exception.verb).to.eq('be raised')

    def test_matches(self):
        expect(ExceptionMatcher(lambda: 1 / 0, ZeroDivisionError).matches()).to.eq(True)
        expect(ExceptionMatcher(lambda: 1 / 0, Exception).matches()).to.eq(True)
        expect(ExceptionMatcher(lambda: None, Exception).matches()).to.eq(False)

    def test_actual_is_not_callable(self):
        self.assertRaises(TypeError, ExceptionMatcher(None, Exception).matches)

    def test_explanation_message_with_wrong_exception(self):
        exception_raised = ExceptionMatcher(lambda: self.raise_exception(TypeError()), ZeroDivisionError)
        message = exception_raised.explanation.message
        expect(message) == """
A = 'ZeroDivisionError'
Z = 'TypeError'
Expected A to be raised
Actually raised Z
"""

    def test_negative_explanation_message_with_wrong_exception(self):
        exception_raised = ExceptionMatcher(
            lambda: self.raise_exception(ZeroDivisionError()), ZeroDivisionError, is_negative=True)
        message = exception_raised.explanation.message
        expect(message) == """
A = 'ZeroDivisionError'
Expected A not to be raised
But it happened
"""

    def test_explanation_message_with_no_exception_was_raised(self):
        no_exception = ExceptionMatcher(lambda: None, Exception)
        message = no_exception.explanation.message
        expect(message) == """
A = 'Exception'
Z = 'nothing'
Expected A to be raised
Actually raised Z
"""

    def test_register(self):
        expect(expect.matcher('throw')) == ExceptionMatcher


class TestExactExceptionMatcher(TestCase):
    def raise_exception(self, ex):
        raise ex

    def test_verb(self):
        exception = ExactExceptionMatcher(lambda: 1 + 1)
        expect(exception.verb).to.eq('be exactly raised')

    def test_matches(self):
        expect(ExactExceptionMatcher(lambda: 1 / 0, ZeroDivisionError).matches()).to.eq(True)
        expect(ExactExceptionMatcher(lambda: 1 / 0, Exception).matches()).to.eq(False)

    def test_explanation_message_with_wrong_exception(self):
        exception_raised = ExactExceptionMatcher(lambda: self.raise_exception(TypeError()), ZeroDivisionError)
        message = exception_raised.explanation.message
        expect(message) == """
A = 'ZeroDivisionError'
Z = 'TypeError'
Expected A to be exactly raised
Actually exactly raised Z
"""

    def test_negative_explanation_message_with_wrong_exception(self):
        exception_raised = ExactExceptionMatcher(
            lambda: self.raise_exception(ZeroDivisionError()), ZeroDivisionError, is_negative=True)
        message = exception_raised.explanation.message
        expect(message) == """
A = 'ZeroDivisionError'
Expected A not to be exactly raised
But it happened
"""

    def test_explanation_message_with_no_exception_was_raised(self):
        no_exception = ExactExceptionMatcher(lambda: None, Exception)
        message = no_exception.explanation.message
        expect(message) == """
A = 'Exception'
Z = 'nothing'
Expected A to be exactly raised
Actually exactly raised Z
"""

    def test_register(self):
        expect(expect.matcher('throw_exactly')) == ExactExceptionMatcher
