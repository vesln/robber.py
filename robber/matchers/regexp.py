import re
from robber import expect
from base import Base

"""
expect('foo').to.match(r'foo')
"""
class Match(Base):
    def matches(self):
        return bool(re.match(self.expected, self.actual))

    def failure_message(self):
        return 'Expected "%s" to match "%s"' % (self.actual, self.expected)

"""
expect('bar').to.not_match(r'foo')
"""
class NotMatch(Base):
    def matches(self):
        return not re.match(self.expected, self.actual)

    def failure_message(self):
        return 'Expected "%s" to not match "%s"' % (self.actual, self.expected)

expect.register('match', Match)
expect.register('not_match', NotMatch)
