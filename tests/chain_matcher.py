from robber.expect import expect
from robber.matchers.base import Base


class Chain(Base):
    def matches(self):
        expectation = self.actual(None)
        chain = getattr(expectation, self.expected)
        return expectation is chain

    def failure_message(self):
        return 'Expected "%s" to have chain "%s"' % (self.actual, self.expected)


expect.register('chain', Chain)
