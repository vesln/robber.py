from robber import expect
from robber.matchers.base import Base


class TrueMatcher(Base):
    """
    expect(true).to.be.true()
    """

    def matches(self):
        return self.actual is True

    def failure_message(self):
        negated_message = ' not' if self.is_negated else ''
        return 'Expected %s%s to be True' % (self.actual, negated_message)


class FalseMatcher(Base):
    """
    expect(false).to.be.false()
    """

    def matches(self):
        return self.actual is False

    def failure_message(self):
        negated_message = ' not' if self.is_negated else ''
        return 'Expected %s%s to be False' % (self.actual, negated_message)


expect.register('true', TrueMatcher)
expect.register('false', FalseMatcher)
