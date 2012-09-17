from robber import expect
from base import Base

class Truthy(Base):
    """
    expect('str').to.be.truthy()
    """
    def matches(self):
        return bool(self.actual)

    def failure_message(self):
        return 'Expected "%s" to be truthy' % self.actual

class Falsy(Base):
    """
    expect('').to.be.falsy()
    """
    def matches(self):
        return not bool(self.actual)

    def failure_message(self):
        return 'Expected "%s" to be falsy' % self.actual

expect.register('truthy', Truthy)
expect.register('falsy', Falsy)
