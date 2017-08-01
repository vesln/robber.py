from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class Identical(Base):
    """
    expect(1).to.equal(1)
    """

    def matches(self):
        return self.actual is self.expected

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be', self.expected)


expect.register('equal', Identical)
