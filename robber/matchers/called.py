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
        return 'Expected {actual}{negated_message} to be called'.format(
            actual=self.actual, negated_message=self.negated_message
        )


expect.register('called', Called)
