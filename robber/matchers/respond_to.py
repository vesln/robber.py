from robber import expect
from robber.matchers.base import Base


class RespondTo(Base):
    """
    expect(obj).to.respond_to('method')
    """

    def matches(self):
        return hasattr(self.actual, self.expected) and callable(getattr(self.actual, self.expected))

    def failure_message(self):
        return 'Expected "{actual}"{negative_message} to respond to "{expected}"'.format(
            actual=self.actual, negative_message=self.negative_message, expected=self.expected
        )


expect.register('respond_to', RespondTo)
