from robber import expect
from base import Base

class Length(Base):
    """
    expect('str').to.have.length(3)
    expect([1, 2, 3]).to.have.length(3)
    """
    def matches(self):
        return len(self.actual) == self.expected

    def failure_message(self):
        return 'Expected "%s" to have a length of %d' % (self.actual, self.expected)

class Empty(Base):
    """
    expect('').to.be.empty()
    expect([]).to.be.empty()
    """
    def matches(self):
        return len(self.actual) == 0

    def failure_message(self):
        return 'Expected "%s" to be empty' % self.actual

expect.register('length', Length)
expect.register('empty', Empty)
