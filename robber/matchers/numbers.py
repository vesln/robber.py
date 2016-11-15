from robber import BadExpectation
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


class Change(Base):
    def __init__(self, callable, obj=None, *args):
        self.callable = callable
        self.obj = obj
        self.args = args
        self.message = None

    def match(self):
        return self

    def by(self, amount=0):
        changed = self.callable(self.obj) - self.obj

        if changed != amount:
            message = self.message or self.failure_message(self.obj, amount, changed)
            raise BadExpectation(message)

        return expect(self.obj)

    def failure_message(self, obj, changed, got):
        return 'Expected %g to be changed by %g, but was changed by %g' % (obj, changed, got)


expect.register('above', Above)
expect.register('below', Below)
expect.register('more_than', Above)
expect.register('less_than', Below)
expect.register('greater_than', Above)
expect.register('smaller_than', Below)
expect.register('within', Within)
expect.register('change', Change)
