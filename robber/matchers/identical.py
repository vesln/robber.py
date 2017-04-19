from robber import expect
from robber.matchers.base import Base


class Identical(Base):
    """
    expect(1).to.equal(1)
    """

    def matches(self):
        return self.actual is self.expected

    def failure_message(self):
        return 'Expected "{actual}"{negative_message} to be "{expected}"'.format(
            actual=self.actual, negative_message=self.negative_message, expected=self.expected
        )


expect.register('equal', Identical)
