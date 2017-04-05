from robber import expect
from robber.matchers.base import Base


class Contain(Base):
    """
    expect({'key': value}).to.contain('key')
    expect([1, 2, 3]).to.contain(2)
    """

    def matches(self):
        return self.expected in self.actual

    def failure_message(self):
        if self.is_negative:
            verb = 'exclude'
        else:
            verb = 'contain'

        message = 'Expected {actual} to {verb} {expected}'

        return message.format(actual=self.actual, verb=verb, expected=self.expected)


expect.register('contain', Contain)
expect.register('exclude', Contain, is_negative=True)
