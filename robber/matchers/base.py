from robber.bad_expectation import BadExpectation

class Base:
    """
    Base matcher. All matchers inherit from it.
    If you want to create a custom matcher, it's a good
    idea to extend it, as well.
    """

    def __init__(self, actual, expected = None, *args):
        self.actual = actual
        self.expected = expected
        self.args = args

    def fail_with(self, message):
        self.message = message
        return self

    def match(self):
        if not self.matches():
            message = self.message or self.failure_message()
            raise BadExpectation, message
