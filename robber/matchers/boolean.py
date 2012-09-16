from robber import expect
from base import Base

"""
expect(true).to.be.true()
"""
class TrueMatcher(Base):
    def matches(self):
        return self.actual == True

    def failure_message(self):
        return 'Expected %s to be True' % self.actual

"""
expect(false).to.be.false()
"""
class FalseMatcher(Base):
    def matches(self):
        return self.actual != True

    def failure_message(self):
        return 'Expected %s to be False' % self.actual

expect.register('true', TrueMatcher)
expect.register('false', FalseMatcher)
