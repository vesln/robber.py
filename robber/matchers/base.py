from robber.bad_expectation import BadExpectation

class Base:
    def __init__(self, actual, expected):
        self.actual = actual
        self.expected = expected

    def match(self):
        if not self.matches():
            raise BadExpectation, self.failure_message()
