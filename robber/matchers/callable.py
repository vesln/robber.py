from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class Callable(Base):
    """
    expect(object).to.be.callable()
    """

    def matches(self):
        return callable(self.actual)

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be callable')


expect.register('callable', Callable)
