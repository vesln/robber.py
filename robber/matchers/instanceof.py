from robber import expect
from base import Base

"""
expect(obj).to.be.an.instanceof(Klass)
"""
class Instanceof(Base):
    def matches(self):
        return isinstance(self.actual, self.expected)

    def failure_message(self):
        return 'Expected "%s" to be an instance of "%s"' % (self.actual, self.expected)

expect.register('instanceof', Instanceof)
