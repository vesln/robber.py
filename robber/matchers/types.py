from robber import expect
from base import Base

class String(Base):
    def matches(self):
        return isinstance(self.actual, str)

    def failure_message(self):
        return 'Expected "%s" to be a string' % self.actual

class Integer(Base):
    def matches(self):
        return isinstance(self.actual, int)

    def failure_message(self):
        return 'Expected "%s" to be an integer' % self.actual

class Float(Base):
    def matches(self):
        return isinstance(self.actual, float)

    def failure_message(self):
        return 'Expected "%s" to be a floating point number' % self.actual

class List(Base):
    def matches(self):
        return isinstance(self.actual, list)

    def failure_message(self):
        return 'Expected "%s" to be an array' % self.actual

class Dict(Base):
    def matches(self):
        return isinstance(self.actual, dict)

    def failure_message(self):
        return 'Expected "%s" to be a dictionary' % self.actual

class Tuple(Base):
    def matches(self):
        return isinstance(self.actual, tuple)

    def failure_message(self):
        return 'Expected "%s" to be a tuple' % self.actual

expect.register('string', String)
expect.register('integer', Integer)
expect.register('float', Float)
expect.register('list', List)
expect.register('dict', Dict)
expect.register('tuple', Tuple)
