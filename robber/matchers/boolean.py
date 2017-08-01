from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class Boolean(Base):
    """
    expect(true).to.be.true()
    expect(true).to.be.false()
    """

    def matches(self):
        return self.actual is True

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be True', negative_action='be False')


expect.register('true', Boolean)
expect.register('false', Boolean, is_negative=True)
