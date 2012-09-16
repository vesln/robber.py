from robber import expect
from base import Base

"""
expect('str').to.be.a.string()
"""
class String(Base):
    def matches(self):
        return isinstance(self.actual, str)

    def failure_message(self):
        return 'Expected "%s" to be a string' % self.actual

"""
expect(1).to.be.a.integer()
"""
class Integer(Base):
    def matches(self):
        return isinstance(self.actual, int)

    def failure_message(self):
        return 'Expected "%s" to be an integer' % self.actual

"""
expect(1.0).to.be.a.float()
"""
class Float(Base):
    def matches(self):
        return isinstance(self.actual, float)

    def failure_message(self):
        return 'Expected "%s" to be a floating point number' % self.actual

"""
expect([]).to.be.a.list()
"""
class List(Base):
    def matches(self):
        return isinstance(self.actual, list)

    def failure_message(self):
        return 'Expected "%s" to be an array' % self.actual

"""
expect({}).to.be.a.dict()
"""
class Dict(Base):
    def matches(self):
        return isinstance(self.actual, dict)

    def failure_message(self):
        return 'Expected "%s" to be a dictionary' % self.actual

"""
expect((1, 2)).to.be.a.tuple()
"""
class Tuple(Base):
    def matches(self):
        return isinstance(self.actual, tuple)

    def failure_message(self):
        return 'Expected "%s" to be a tuple' % self.actual

"""
expect(None).to.be.none()
"""
class Non(Base):
    def matches(self):
        return self.actual == None

    def failure_message(self):
        return 'Expected "%s" to be None' % self.actual

expect.register('string', String)
expect.register('integer', Integer)
expect.register('float', Float)
expect.register('list', List)
expect.register('dict', Dict)
expect.register('tuple', Tuple)
expect.register('none', Non)
