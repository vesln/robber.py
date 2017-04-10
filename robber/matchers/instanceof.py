from robber import expect
from robber.matchers.base import Base


class Instanceof(Base):
    """
    expect(obj).to.be.an.instanceof(Klass)
    """

    def matches(self):
        return isinstance(self.actual, self.expected)

    def failure_message(self):
        return 'Expected "{actual}"{negative_message} to be an instance of "{expected}"'.format(
            actual=self.actual, negative_message=self.negative_message, expected=self.expected
        )


expect.register('instanceof', Instanceof)
