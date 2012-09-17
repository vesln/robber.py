from robber import expect
from base import Base

class String(Base):
    """
    expect('str').to.be.a.string()
    """
    def matches(self):
        return isinstance(self.actual, str)

    def failure_message(self):
        return 'Expected "%s" to be a string' % self.actual

class Integer(Base):
    """
    expect(1).to.be.a.integer()
    """
    def matches(self):
        return isinstance(self.actual, int)

    def failure_message(self):
        return 'Expected "%s" to be an integer' % self.actual

class Float(Base):
    """
    expect(1.0).to.be.a.float()
    """
    def matches(self):
        return isinstance(self.actual, float)

    def failure_message(self):
        return 'Expected "%s" to be a floating point number' % self.actual

class List(Base):
    """
    expect([]).to.be.a.list()
    """
    def matches(self):
        return isinstance(self.actual, list)

    def failure_message(self):
        return 'Expected "%s" to be an array' % self.actual

class Dict(Base):
    """
    expect({}).to.be.a.dict()
    """
    def matches(self):
        return isinstance(self.actual, dict)

    def failure_message(self):
        return 'Expected "%s" to be a dictionary' % self.actual

class Tuple(Base):
    """
    expect((1, 2)).to.be.a.tuple()
    """
    def matches(self):
        return isinstance(self.actual, tuple)

    def failure_message(self):
        return 'Expected "%s" to be a tuple' % self.actual

class Non(Base):
    """
    expect(None).to.be.none()
    """
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
