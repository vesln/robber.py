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
        return 'Expected "{actual}"{negated_message} to equal "{expected}"'.format(
            actual=self.actual, expected=self.expected, negated_message=self.negated_message
        )


class NotEqual(Base):
    """
    expect(1).to.ne(2)
    expect(1).to.not_eq(2)
    expect(1).to != 2
    expect(2) 1= 2
    """

    def matches(self):
        return self.actual != self.expected

    def failure_message(self):
        return 'Expected "{actual}"{negated_message} not to equal "{expected}"'.format(
            actual=self.actual, expected=self.expected, negated_message=self.negated_message
        )


expect.register('eq', Equal)
expect.register('__eq__', Equal)

expect.register('ne', NotEqual)
expect.register('__ne__', NotEqual)
expect.register('not_eq', NotEqual)
