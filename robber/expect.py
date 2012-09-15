from bad_expectation import BadExpectation

class expect:
    def __init__(self, object):
        self.object = object
        self.__setup_chaining()

    @classmethod
    def register(self, name, klass):
        method = lambda self, other=None: klass(self.object, other).match()
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

    def __setup_chaining(self):
        self.to = self
        self.be = self
