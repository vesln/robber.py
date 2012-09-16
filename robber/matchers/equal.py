from robber import expect
from base import Base

"""
expect(1).to.eq(1)
expect(1).to == 1
expect(1) == 1
"""
class Equal(Base):
    def matches(self):
        return self.actual == self.expected

    def failure_message(self):
        return 'Expected "%s" to equal "%s"' % (self.actual, self.expected)

"""
expect(1).to.ne(2)
expect(1).to.not_eq(2)
expect(1).to != 2
expect(2) 1= 2
"""
class NotEqual(Base):
    def matches(self):
        return self.actual != self.expected

    def failure_message(self):
        return 'Expected "%s" to not equal "%s"' % (self.actual, self.expected)

expect.register('eq', Equal)
expect.register('__eq__', Equal)

expect.register('ne', NotEqual)
expect.register('__ne__', NotEqual)
expect.register('not_eq', NotEqual)
