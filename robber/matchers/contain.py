from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class Contain(Base):
    """
    expect({'key': value}).to.contain('key')
    expect([1, 2, 3]).to.contain(2)
    """

    def matches(self):
        return self.expected in self.actual

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'contain', self.expected, negative_action='exclude')


expect.register('contain', Contain)
expect.register('exclude', Contain, is_negative=True)
