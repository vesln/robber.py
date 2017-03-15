from robber import expect
from robber.matchers.base import Base


class Callable(Base):
    """
    expect(function).to.be.callable()
    """

    def matches(self):
        return hasattr(self.actual, '__call__')

    def failure_message(self):
        return 'Expected {actual} to be callable'.format(actual=self.actual)


expect.register('callable', Callable)
expect.register('__callable__', Callable)
