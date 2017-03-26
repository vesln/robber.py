class BadExpectation(Exception):
    """
    Raised when an assertion fails.
    """

    def __init__(self, message):
        self.message = message
