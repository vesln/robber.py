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
            raise TypeError('{function} is not a mock'.format(function=self.actual))

    def failure_message(self):
        return 'Expected {function} to be called'.format(function=self.actual)


expect.register('called', Called)
expect.register('__called__', Called)
