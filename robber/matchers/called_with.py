from mock import call

from robber import expect
from robber.matchers.base import Base


class CalledWith(Base):
    """
    expect(mock).to.be.called_with(*args)
    """

    def matches(self):
        try:
            return self.actual.called and self.actual.call_args == call(self.expected)
        except AttributeError:
            raise TypeError('{actual} is not a mock'.format(actual=self.actual))

    def failure_message(self):
        return 'Expected {actual} to be called with {args}'.format(actual=self.actual, args=self.expected)


expect.register('called_with', CalledWith)
expect.register('__called_with__', CalledWith)
