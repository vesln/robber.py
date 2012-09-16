from robber import expect
from base import Base

"""
expect('str').to.be.truthy()
"""
class Truthy(Base):
    def matches(self):
        return bool(self.actual)

    def failure_message(self):
        return 'Expected "%s" to be truthy' % self.actual

"""
expect('').to.be.falsy()
"""
class Falsy(Base):
    def matches(self):
        return not bool(self.actual)

    def failure_message(self):
        return 'Expected "%s" to be falsy' % self.actual

expect.register('truthy', Truthy)
expect.register('falsy', Falsy)
