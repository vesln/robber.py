from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class Length(Base):
    """
    expect('str').to.have.length(3)
    expect([1, 2, 3]).to.have.length(3)
    """

    def matches(self):
        return len(self.actual) == self.expected

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'have length of', self.expected)


class Empty(Base):
    """
    expect('').to.be.empty()
    expect([]).to.be.empty()
    """

    def matches(self):
        return len(self.actual) == 0

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be empty')


expect.register('length', Length)
expect.register('empty', Empty)
