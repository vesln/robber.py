from robber.expect import expect
from robber.matchers.base import Base

class TrueMatcher(Base):
    def failure_message(self):
        return 'Expected %s to be True' % self.actual

    def matches(self):
        return self.actual == True

class FalseMatcher(Base):
    def failure_message(self):
        return 'Expected %s to be False' % self.actual

    def matches(self):
        return self.actual != True

expect.register('true', TrueMatcher)
expect.register('false', FalseMatcher)
