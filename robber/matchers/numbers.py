from robber import expect
from robber.matchers.base import Base


class Above(Base):
    """
    expect(2).to.be.above(1)
    """
    def matches(self):
        return self.actual > self.expected

    def failure_message(self):
        return 'Expected %g to be above %g' % (self.actual, self.expected)


class Below(Base):
    """
    expect(1).to.be.below(2)
    """
    def matches(self):
        return self.actual < self.expected

    def failure_message(self):
        return 'Expected %g to be below %g' % (self.actual, self.expected)


class Within(Base):
    """
    expect(1).to.be.within(0, 2)
    """
    def matches(self):
        return self.expected <= self.actual <= self.args[0]

    def failure_message(self):
        return 'Expected %g to be within %g and %g' % (self.actual, self.expected, self.args[0])

expect.register('above', Above)
expect.register('below', Below)
expect.register('more_than', Above)
expect.register('less_than', Below)
expect.register('greater_than', Above)
expect.register('smaller_than', Below)
expect.register('within', Within)
