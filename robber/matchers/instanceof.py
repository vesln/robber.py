from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class InstanceOf(Base):
    """
    expect(obj).to.be.an.instanceof(Klass)
    """

    def matches(self):
        return isinstance(self.actual, self.expected)

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be an instance of', self.expected)


expect.register('instanceof', InstanceOf)
