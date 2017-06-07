from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class ExceptionMatcher(Base):
    """
    expect(lambda: call_something(with_some_params)).to.throw(any_exception)
    """

    @property
    def raised(self):
        try:
            return self._raised
        except AttributeError:
            if not callable(self.actual):
                raise TypeError('{actual} is not callable'.format(actual=self.actual))

            try:
                self.actual()
            except BaseException as raised:
                self._raised = raised
                return self._raised

    def matches(self):
        return isinstance(self.raised, self.expected)

    @property
    def verb(self):
        return 'be raised'

    @property
    def explanation(self):
        if self.raised:
            got = self.raised.__class__.__name__
        else:
            got = 'nothing'

        return Explanation(self.expected.__name__, self.is_negative, self.verb, other=got)


class ExactExceptionMatcher(ExceptionMatcher):
    """
    expect(lambda: call_something(with_some_params)).to.throw_exactly(any_exception)
    """

    def matches(self):
        return type(self.raised) == self.expected

    @property
    def verb(self):
        return 'be exactly raised'


expect.register('throw', ExceptionMatcher)
expect.register('throw_exactly', ExactExceptionMatcher)
