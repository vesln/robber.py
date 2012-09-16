from robber import expect
from base import Base

class TrueMatcher(Base):
    def matches(self):
        return self.actual == True

    def failure_message(self):
        return 'Expected %s to be True' % self.actual

class FalseMatcher(Base):
    def matches(self):
        return self.actual != True

    def failure_message(self):
        return 'Expected %s to be False' % self.actual

expect.register('true', TrueMatcher)
expect.register('false', FalseMatcher)
