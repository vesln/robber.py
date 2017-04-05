from robber import expect
from robber.matchers.base import Base


class Equal(Base):
    """
    expect(1).to.eq(1)
    expect(1).to == 1
    expect(1) == 1
    """

    def matches(self):
        return self.actual == self.expected

    def failure_message(self):
        return 'Expected "{actual}"{negative_message} to equal "{expected}"'.format(
            actual=self.actual, expected=self.expected, negative_message=self.negative_message
        )


expect.register('eq', Equal)
expect.register('__eq__', Equal)

expect.register('ne', Equal, is_negative=True)
expect.register('__ne__', Equal, is_negative=True)
