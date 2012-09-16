class expect:
    matchers = {}
    message = None

    def __init__(self, object):
        self.object = object
        self.__setup_chaining()

    @classmethod
    def fail_with(self, message):
        self.message = message

    @classmethod
    def remove_custom_message(self):
        self.message = None

    @classmethod
    def register(self, name, klass):
        self.matchers[name] = klass
        method = lambda self, other=None, *args: \
                klass(self.object, other, *args) \
                    .fail_with(self.message) \
                    .match()

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

- inline docs
"""
