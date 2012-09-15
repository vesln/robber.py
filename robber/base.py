class BadExpectation(Exception):
    pass

class expect:
    def __init__(self, object):
        self.object = object
        self.__setup_chaining()

    @classmethod
    def register(self, name, klass):
        method = lambda self, other=None: klass(self.object, other)
        setattr(self, name, method)

    @classmethod
    def unregister(self, name):
        delattr(self, name)
        pass

    @classmethod
    def registered(self, name):
        try:
            getattr(self, name)
        except AttributeError:
            return False
        else:
            return True

    def eq(self, other):
        assertion = self.object == other
        message = 'Expected "%s" to equal "%s"' % (self.object, other)

        self.__assert(assertion, message)

    def not_eq(self, other):
        assertion = self.object != other
        message = 'Expected "%s" to not equal "%s"' % (self.object, other)

        self.__assert(assertion, message)

    def ne(self, other):
        self.not_eq(other)

    def equal(self, other):
        assertion = self.object is other
        message = 'Expected "%s" to be "%s"' % (self.object, other)

        self.__assert(assertion, message)

    def not_equal(self, other):
        assertion = self.object is not other
        message = 'Expected "%s" to not be "%s"' % (self.object, other)

        self.__assert(assertion, message)

    def __eq__(self, other):
        self.eq(other)
        return True

    def __ne__(self, other):
        self.not_eq(other)
        return True

    def __setup_chaining(self):
        self.to = self
        self.be = self

    def __assert(self, expected, message):
        if not expected:
            raise BadExpectation(message)

# TODO:
# - move messages to a class
# - alias decorator
