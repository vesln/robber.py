from robber import expect
from robber.matchers.base import Base


class Callable(Base):
    """
    expect(object).to.be.callable()
    """

    def matches(self):
        return callable(self.actual)

    def failure_message(self):
        return 'Expected {actual}{negative_message} to be callable'.format(
            actual=self.actual, negative_message=self.negative_message
        )


expect.register('callable', Callable)
