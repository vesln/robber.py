from termcolor import colored


class BadExpectation(Exception):
    """
    Raised when an assertion fails.
    """

    def __init__(self, message):
        super(BadExpectation, self).__init__(message)
        self.message = message

    def __str__(self):
        return colored(self.message, 'red')
