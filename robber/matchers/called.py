from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class Called(Base):
    """
    expect(mock).to.be.called()
    """

    def matches(self):
        try:
            return self.actual.called
        except AttributeError:
            raise TypeError('{actual} is not a mock'.format(actual=self.actual))

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be called')


expect.register('called', Called)
