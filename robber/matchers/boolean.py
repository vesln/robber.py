from robber import expect
from robber.matchers.base import Base


class TrueMatcher(Base):
    """
    expect(true).to.be.true()
    """

    def matches(self):
        return self.actual is True

    def failure_message(self):
        return 'Expected {actual}{negated_message} to be True'.format(
            actual=self.actual, negated_message=self.negated_message
        )


class FalseMatcher(Base):
    """
    expect(false).to.be.false()
    """

    def matches(self):
        return self.actual is False

    def failure_message(self):
        return 'Expected {actual}{negated_message} to be False'.format(
            actual=self.actual, negated_message=self.negated_message
        )


expect.register('true', TrueMatcher)
expect.register('false', FalseMatcher)
