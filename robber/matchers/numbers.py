from robber import expect
from base import Base

class Above(Base):
    """
    expect(2).to.be.above(1)
    """
    def matches(self):
        return self.actual > self.expected

    def failure_message(self):
        return 'Expected %d to be above %d' % (self.actual, self.expected)

class Below(Base):
    """
    expect(1).to.be.below(2)
    """
    def matches(self):
        return self.actual < self.expected

    def failure_message(self):
        return 'Expected %d to be below %d' % (self.actual, self.expected)

class Within(Base):
    """
    expect(1).to.be.within(0, 2)
    """
    def matches(self):
        return self.expected <= self.actual <= self.args[0]

    def failure_message(self):
        return 'Expected %d to be within %d and %d' % (self.actual, self.expected, self.args[0])

expect.register('above', Above)
expect.register('below', Below)
expect.register('within', Within)
