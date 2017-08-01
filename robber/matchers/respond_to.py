from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class RespondTo(Base):
    """
    expect(obj).to.respond_to('method')
    """

    def matches(self):
        return hasattr(self.actual, self.expected) and callable(getattr(self.actual, self.expected))

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'respond to', self.expected)


expect.register('respond_to', RespondTo)
