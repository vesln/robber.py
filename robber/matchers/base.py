from robber.bad_expectation import BadExpectation
from robber.expect import expect


class Base:
    """
    Base matcher. All matchers inherit from it.
    If you want to create a custom matcher, it's a good
    idea to extend it, as well.
    """

    def __init__(self, actual, expected=None, is_negated=False, *args):
        self.actual = actual
        self.expected = expected
        self.is_negated = is_negated
        self.args = args

    def fail_with(self, message):
        self.message = message
        return self

    def match(self):
        if not (self.matches() or self.is_negated):
            message = self.message or self.failure_message()
            raise BadExpectation(message)

        return expect(self.actual)
