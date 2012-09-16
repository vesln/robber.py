from robber.expect import expect
from base import Base

class Length(Base):
    def matches(self):
        return len(self.actual) == self.expected

    def failure_message(self):
        return 'Expected "%s" to have a length of %d' % (self.actual, self.expected)

class Empty(Base):
    def matches(self):
        return len(self.actual) == 0

    def failure_message(self):
        return 'Expected "%s" to be empty' % self.actual

expect.register('length', Length)
expect.register('empty', Empty)
