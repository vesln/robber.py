from robber.expect import expect
from robber.matchers.base import Base

class Identical(Base):
    def matches(self):
        return self.actual is self.expected

    def failure_message(self):
        return 'Expected "%s" to be "%s"' % (self.actual, self.expected)

class NotIdentical(Base):
    def matches(self):
        return self.actual is not self.expected

    def failure_message(self):
        return 'Expected "%s" to not be "%s"' % (self.actual, self.expected)

expect.register('equal', Identical)
expect.register('not_equal', NotIdentical)
