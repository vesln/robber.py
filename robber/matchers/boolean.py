from robber import expect
from base import Base

class TrueMatcher(Base):
    """
    expect(true).to.be.true()
    """

    def matches(self):
        return self.actual == True

    def failure_message(self):
        return 'Expected %s to be True' % self.actual

class FalseMatcher(Base):
    """
    expect(false).to.be.false()
    """

    def matches(self):
        return self.actual != True

    def failure_message(self):
        return 'Expected %s to be False' % self.actual

expect.register('true', TrueMatcher)
expect.register('false', FalseMatcher)
