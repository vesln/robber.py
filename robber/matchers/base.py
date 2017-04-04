from robber.bad_expectation import BadExpectation
from robber.expect import expect


class Base:
    """
    Base matcher. All matchers inherit from it.
    If you want to create a custom matcher, it's a good
    idea to extend it, as well.
    """

    def __init__(self, actual, expected=None, is_negative=False, *args):
        self.actual = actual
        self.expected = expected
        self.is_negative = is_negative
        self.args = args
        self.message = None

    def fail_with(self, message):
        self.message = message
        return self

    def match(self):
        if self.matches() == (not self.is_negative):
            return expect(self.actual)

        message = self.message or self.failure_message()
        raise BadExpectation(message)

    @property
    def negative_message(self):
        if self.is_negative:
            return ' not'
        return ''
