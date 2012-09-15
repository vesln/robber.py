from robber.expect import expect
from robber.matchers.base import Base

class Instanceof(Base):
    def failure_message(self):
        return 'Expected "%s" to be an instance of "%s"' % (self.actual, self.expected)

    def matches(self):
        return isinstance(self.actual, self.expected)

expect.register('instanceof', Instanceof)
