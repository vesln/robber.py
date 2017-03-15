from robber import expect
from robber.matchers.base import Base


class Called(Base):
    """
    expect(function).to.be.called()
    """

    def matches(self):
        try:
            return self.actual.called
        except AttributeError:
            raise TypeError('{actual} is not a mock'.format(actual=self.actual))

    def failure_message(self):
        return 'Expected {actual} to be called'.format(actual=self.actual)


class CalledOnce(Base):
    """
    expect(function).to.be.called_once()
    """

    def matches(self):
        try:
            return self.actual.call_count == 1
        except AttributeError:
            raise TypeError('{actual} is not a mock'.format(actual=self.actual))

    def failure_message(self):
        return 'Expected {actual} to be called once'.format(actual=self.actual)


expect.register('called', Called)
expect.register('__called__', Called)
expect.register('called_once', CalledOnce)
expect.register('__called_once__', CalledOnce)
