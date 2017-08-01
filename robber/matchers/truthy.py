from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class Truthy(Base):
    """
    expect('str').to.be.truthy()
    expect('str').to.be.falsy()
    """

    def matches(self):
        return bool(self.actual)

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, action='be truthy', negative_action='be falsy')


expect.register('truthy', Truthy)
expect.register('falsy', Truthy, is_negative=True)
