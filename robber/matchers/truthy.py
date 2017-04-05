from robber import expect
from robber.matchers.base import Base


class Truthy(Base):
    """
    expect('str').to.be.truthy()
    """

    def matches(self):
        return bool(self.actual)

    def failure_message(self):
        message = 'Expected "{actual}" to be {adj}'

        if not self.is_negative:
            adj = 'truthy'
        else:
            adj = 'falsy'

        return message.format(actual=self.actual, adj=adj)


expect.register('truthy', Truthy)
expect.register('falsy', Truthy, is_negative=True)
