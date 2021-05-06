from robber import BadExpectation
from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class Above(Base):
    """
    expect(2).to.be.above(1)
    """

    def matches(self):
        return self.actual > self.expected

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be above', self.expected)


class Below(Base):
    """
    expect(1).to.be.below(2)
    """

    def matches(self):
        return self.actual < self.expected

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be below', self.expected)


class AboveEqual(Base):
    """
    expect(2).to.be.above_or_equal(1)
    """

    def matches(self):
        return self.actual >= self.expected

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be above of or equal to', self.expected)


class BelowEqual(Base):
    """
    expect(1).to.be.below_or_equal(2)
    """

    def matches(self):
        return self.actual <= self.expected

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be below of or equal to', self.expected)


class Within(Base):
    """
    expect(1).to.be.within(0, 2)
    """

    def matches(self):
        return self.expected <= self.actual <= self.args[0]

    @property
    def explanation(self):
        return Explanation(
            self.actual, self.is_negative, 'be within', self.expected, 'and', self.args[0]
        )


class Change(Base):
    def __init__(self, callable, obj=None, is_negative=False, *args):
        self.callable = callable
        self.obj = obj
        self.args = args
        self.message = None
        self.is_negative = is_negative

    def match(self):
        return self

    def by(self, amount=0):
        self.changed = self.callable(self.obj) - self.obj
        self.amount = amount
        message = self.message or self.explanation.message

        if (self.changed == amount) == (not self.is_negative):
            return True

        raise BadExpectation(message)

    @property
    def explanation(self):
        return Explanation(
            self.callable.__name__, self.is_negative, 'change', self.obj,
            another_action='by', another_expected=self.amount,
            other=self.changed, force_disable_repr=True
        )


expect.register('above', Above)
expect.register('below', Below)
expect.register('more_than', Above)
expect.register('less_than', Below)
expect.register('greater_than', Above)
expect.register('smaller_than', Below)
expect.register('above_or_equal', AboveEqual)
expect.register('below_or_equal', BelowEqual)
expect.register('more_than_or_equal_to', AboveEqual)
expect.register('less_than_or_equal_to', BelowEqual)
expect.register('greater_than_or_equal_to', AboveEqual)
expect.register('smaller_than_or_equal_to', BelowEqual)
expect.register('within', Within)
expect.register('change', Change)
