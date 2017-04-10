from robber import expect
from robber.matchers.base import Base


class Length(Base):
    """
    expect('str').to.have.length(3)
    expect([1, 2, 3]).to.have.length(3)
    """

    def matches(self):
        return len(self.actual) == self.expected

    def failure_message(self):
        return 'Expected "{actual}"{negative_message} to have a length of {expected}'.format(
            actual=self.actual, negative_message=self.negative_message, expected=self.expected
        )


class Empty(Base):
    """
    expect('').to.be.empty()
    expect([]).to.be.empty()
    """

    def matches(self):
        return len(self.actual) == 0

    def failure_message(self):
        return 'Expected "{actual}"{negative_message} to be empty'.format(
            actual=self.actual, negative_message=self.negative_message
        )


expect.register('length', Length)
expect.register('empty', Empty)
