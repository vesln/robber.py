from robber.expect import expect
from robber.matchers.base import Base

class Truthy(Base):
    def matches(self):
        return bool(self.actual)

    def failure_message(self):
        return 'Expected "%s" to be truthy' % self.actual

class Falsy(Base):
    def matches(self):
        return not bool(self.actual)

    def failure_message(self):
        return 'Expected "%s" to be falsy' % self.actual

expect.register('truthy', Truthy)
expect.register('falsy', Falsy)
