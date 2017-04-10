from robber import expect
from robber.matchers.base import Base


class Boolean(Base):
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


expect.register('true', Boolean)
expect.register('false', Boolean, is_negative=True)
