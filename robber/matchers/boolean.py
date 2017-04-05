from robber import expect
from robber.matchers.base import Base


class TrueMatcher(Base):
    """
    expect(true).to.be.true()
    """

    def matches(self):
        return self.actual is True

    def failure_message(self):
        message = 'Expected {actual} to be {adj}'

        if not self.is_negative:
            adj = 'True'
        else:
            adj = 'False'

        return message.format(actual=self.actual, adj=adj)


expect.register('true', TrueMatcher)
expect.register('false', TrueMatcher, is_negative=True)
