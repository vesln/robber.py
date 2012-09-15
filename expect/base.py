def expect(target):
    return Expectation(target)

class BadExpectation(Exception):
    pass

class Expectation:
    def __init__(self, object):
        self.object = object
        self.__setup_chaining()

    def equal(self, other):
        assertion = self.object == other
        message = 'Expected "%s" to equal "%s"' % (self.object, other)

        self.__assert(assertion, message)

    def not_equal(self, other):
        assertion = self.object != other
        message = 'Expected "%s" to not equal "%s"' % (self.object, other)

        self.__assert(assertion, message)

    def be(self, other):
        assertion = self.object is other
        message = 'Expected "%s" to be "%s"' % (self.object, other)

        self.__assert(assertion, message)

    def not_be(self, other):
        assertion = self.object is not other
        message = 'Expected "%s" to not be "%s"' % (self.object, other)

        self.__assert(assertion, message)

    def __setup_chaining(self):
        self.to = self

    def __assert(self, expected, message):
        if not expected:
            raise BadExpectation(message)

