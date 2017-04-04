from robber import expect
from robber.matchers.base import Base


class Truthy(Base):
    """
    expect('str').to.be.truthy()
    """

    def matches(self):
        return bool(self.actual)

    def failure_message(self):
        return 'Expected "{actual}"{negative_message} to be truthy'.format(
            actual=self.actual, negative_message=self.negative_message
        )


class Falsy(Base):
    """
    expect('').to.be.falsy()
    """

    def matches(self):
        return not bool(self.actual)

    def failure_message(self):
        return 'Expected "{actual}"{negative_message} to be falsy'.format(
            actual=self.actual, negative_message=self.negative_message
        )


expect.register('truthy', Truthy)
expect.register('falsy', Falsy)
