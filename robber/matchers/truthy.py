from robber import expect
from robber.matchers.base import Base


class Truthy(Base):
    """
    expect('str').to.be.truthy()
    """

    def matches(self):
        return bool(self.actual)

    def failure_message(self):
        return 'Expected "{actual}"{negated_message} to be truthy'.format(
            actual=self.actual, negated_message=self.negated_message
        )


class Falsy(Base):
    """
    expect('').to.be.falsy()
    """

    def matches(self):
        return not bool(self.actual)

    def failure_message(self):
        return 'Expected "{actual}"{negated_message} to be falsy'.format(
            actual=self.actual, negated_message=self.negated_message
        )


expect.register('truthy', Truthy)
expect.register('falsy', Falsy)
