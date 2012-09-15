import re
from robber.expect import expect
from robber.matchers.base import Base

class Match(Base):
    def failure_message(self):
        return 'Expected "%s" to match "%s"' % (self.actual, self.expected)

    def matches(self):
        return bool(re.match(self.expected, self.actual))

class NotMatch(Base):
    def failure_message(self):
        return 'Expected "%s" to not match "%s"' % (self.actual, self.expected)

    def matches(self):
        return not re.match(self.expected, self.actual)

expect.register('match', Match)
expect.register('not_match', NotMatch)
