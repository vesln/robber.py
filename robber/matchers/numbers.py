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


class Within(Base):
    """
    expect(1).to.be.within(0, 2)
    """

    def matches(self):
        return self.expected <= self.actual <= self.args[0]

    # def failure_message(self):
    #     return 'Expected {a}{negative_message} to be within {m} and {n}'.format(
    #         a=self.actual, negative_message=self.negative_message, m=self.expected, n=self.args[0]
    #     )

    @property
    def explanation(self):
        return Explanation(
            self.actual, self.is_negative, 'be within', self.expected, self.args[0], additional_action='and'
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
        changed = self.callable(self.obj) - self.obj
        message = self.message or self.failure_message(self.callable.__name__, self.obj, amount, changed)

        if (changed == amount) == (not self.is_negative):
            return expect(self.obj)

        raise BadExpectation(message)

    def failure_message(self, callable_name, obj, changed, got):
        message = 'Expected function {function}{negative_message} to change {a} by {x}, but was changed by {y}'
        return message.format(
            function=callable_name,
            negative_message=self.negative_message,
            a=obj, x=changed, y=got
        )


expect.register('above', Above)
expect.register('below', Below)
expect.register('more_than', Above)
expect.register('less_than', Below)
expect.register('greater_than', Above)
expect.register('smaller_than', Below)
expect.register('within', Within)
expect.register('change', Change)
