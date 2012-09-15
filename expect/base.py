def expect(target):
    return Expectation(target)

class BadExpectation(Exception):
    pass

class Expectation:
    def __init__(self, object):
        self.object = object
        self.__setup_chaining()

    def equal(self, other):
        if self.object != other:
            raise BadExpectation(
                'Expected "%s" to equal "%s"' % (self.object, other)
            )

    def be(self, other):
        if self.object is not other:
            raise BadExpectation(
                'Expected "%s" to be "%s"' % (self.object, other)
            )

    def __setup_chaining(self):
        self.to = self
