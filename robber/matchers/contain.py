from robber import expect
from base import Base

class Contain(Base):
    """
    expect({'key': value}).to.contain('key')
    expect([1, 2, 3]).to.contain(2)
    """
    def matches(self):
        return self.expected in self.actual

    def failure_message(self):
        return 'Expected {0} to contain {1}'.format(self.actual, self.expected)

expect.register('contain', Contain)
