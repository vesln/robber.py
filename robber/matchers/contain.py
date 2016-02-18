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
        return 'Expected {0} to contain {1}'.format(self.actual, self.expected)

class NotContain(Base):
    """
    expect({'key': value}).to.not_contain('other')
    expect([1, 2, 3]).to.not_contain(4)
    """
    def matches(self):
        return self.expected not in self.actual

    def failure_message(self):
        return 'Expected {0} to not contain {1}'.format(self.actual, self.expected)

expect.register('contain', Contain)

expect.register('not_contain', NotContain)
expect.register('exclude', NotContain)
