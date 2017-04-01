from robber import expect
from robber.matchers.base import Base


class Callable(Base):
    """
    expect(function).to.be.callable()
    """

    def matches(self):
        return callable(self.actual)

    def failure_message(self):
        return 'Expected {actual}{negated_message} to be callable'.format(
            actual=self.actual, negated_message=self.negated_message
        )


expect.register('callable', Callable)
