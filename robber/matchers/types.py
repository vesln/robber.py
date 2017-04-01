from robber import expect
from robber.matchers.base import Base


class String(Base):
    """
    expect('str').to.be.a.string()
    """

    def matches(self):
        return isinstance(self.actual, str)

    def failure_message(self):
        return 'Expected "{actual}"{negated_message} to be a string'.format(
            actual=self.actual, negated_message=self.negated_message
        )


class Integer(Base):
    """
    expect(1).to.be.a.integer()
    """

    def matches(self):
        return isinstance(self.actual, int)

    def failure_message(self):
        return 'Expected "{actual}"{negated_message} to be an integer'.format(
            actual=self.actual, negated_message=self.negated_message
        )


class Float(Base):
    """
    expect(1.0).to.be.a.float()
    """

    def matches(self):
        return isinstance(self.actual, float)

    def failure_message(self):
        return 'Expected "{actual}"{negated_message} to be a floating point number'.format(
            actual=self.actual, negated_message=self.negated_message
        )


class List(Base):
    """
    expect([]).to.be.a.list()
    """

    def matches(self):
        return isinstance(self.actual, list)

    def failure_message(self):
        return 'Expected "{actual}"{negated_message} to be an array'.format(
            actual=self.actual, negated_message=self.negated_message
        )


class Dict(Base):
    """
    expect({}).to.be.a.dict()
    """

    def matches(self):
        return isinstance(self.actual, dict)

    def failure_message(self):
        return 'Expected "{actual}"{negated_message} to be a dictionary'.format(
            actual=self.actual, negated_message=self.negated_message
        )


class Tuple(Base):
    """
    expect((1, 2)).to.be.a.tuple()
    """

    def matches(self):
        return isinstance(self.actual, tuple)

    def failure_message(self):
        return 'Expected "{actual}"{negated_message} to be a tuple'.format(
            actual=self.actual, negated_message=self.negated_message
        )


class Non(Base):
    """
    expect(None).to.be.none()
    """

    def matches(self):
        return self.actual is None

    def failure_message(self):
        return 'Expected "{actual}"{negated_message} to be None'.format(
            actual=self.actual, negated_message=self.negated_message
        )


expect.register('string', String)
expect.register('integer', Integer)
expect.register('float', Float)
expect.register('list', List)
expect.register('dict', Dict)
expect.register('tuple', Tuple)
expect.register('none', Non)
