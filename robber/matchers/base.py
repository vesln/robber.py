from robber.bad_expectation import BadExpectation


class Base:
    """
    Base matcher. All matchers inherit from it.
    If you want to create a custom matcher, it's a good
    idea to extend it, as well.
    """

    def __init__(self, actual, expected=None, is_negative=False, *args, **kwargs):
        self.actual = actual
        self.expected = expected
        self.is_negative = is_negative
        self.args = args
        self.kwargs = kwargs
        self.message = None
        self.fail_class = None

    def fail_with(self, message):
        self.message = message
        return self

    def match(self):
        if self.matches() is not self.is_negative:
            return True

        message = self.message or self.explanation.message
        raise BadExpectation(message)

    @property
    def negative_message(self):
        if self.is_negative:
            return ' not'
        return ''
