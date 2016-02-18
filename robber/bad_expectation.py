class BadExpectation(Exception):
    """
    Raised when an assertion fails.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)
