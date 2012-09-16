class expect:
    matchers = {}

    def __init__(self, object):
        self.object = object
        self.__setup_chaining()

    @classmethod
    def register(self, name, klass):
        self.matchers[name] = klass
        method = lambda self, other=None: klass(self.object, other).match()
        setattr(self, name, method)

    @classmethod
    def matcher(self, name):
        return self.matchers[name]

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
        self.to   = self
        self.be   = self
        self.a    = self
        self.an   = self
        self.have = self

"""
TODO:

- None, string, int etc
- above/below/within, close to
- raise
"""
