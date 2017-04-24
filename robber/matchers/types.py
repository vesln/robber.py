from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class String(Base):
    """
    expect('str').to.be.a.string()
    """

    def matches(self):
        return isinstance(self.actual, str)

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be a string')


class Integer(Base):
    """
    expect(1).to.be.a.integer()
    """

    def matches(self):
        return isinstance(self.actual, int)

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be an integer')


class Float(Base):
    """
    expect(1.0).to.be.a.float()
    """

    def matches(self):
        return isinstance(self.actual, float)

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be a floating point number')


class List(Base):
    """
    expect([]).to.be.a.list()
    """

    def matches(self):
        return isinstance(self.actual, list)

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be an array')


class Dict(Base):
    """
    expect({}).to.be.a.dict()
    """

    def matches(self):
        return isinstance(self.actual, dict)

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be a dictionary')


class Tuple(Base):
    """
    expect((1, 2)).to.be.a.tuple()
    """

    def matches(self):
        return isinstance(self.actual, tuple)

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be a tuple')


class Non(Base):
    """
    expect(None).to.be.none()
    """

    def matches(self):
        return self.actual is None

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be None')


expect.register('string', String)
expect.register('integer', Integer)
expect.register('float', Float)
expect.register('list', List)
expect.register('dict', Dict)
expect.register('tuple', Tuple)
expect.register('none', Non)
