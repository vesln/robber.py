from robber.expect import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class Chain(Base):
    def matches(self):
        expectation = self.actual(None)
        chain = getattr(expectation, self.expected)
        return expectation is chain

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'have chain', self.expected)


expect.register('chain', Chain)
