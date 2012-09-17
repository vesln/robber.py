from robber import expect
from base import Base

class Identical(Base):
    """
    expect(1).to.equal(1)
    """

    def matches(self):
        return self.actual is self.expected

    def failure_message(self):
        return 'Expected "%s" to be "%s"' % (self.actual, self.expected)

class NotIdentical(Base):
    """
    expect(1).to.not_equal(2)
    """

    def matches(self):
        return self.actual is not self.expected

    def failure_message(self):
        return 'Expected "%s" not to be "%s"' % (self.actual, self.expected)

expect.register('equal', Identical)
expect.register('not_equal', NotIdentical)
