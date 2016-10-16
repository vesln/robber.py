from robber import expect
from robber.matchers.base import Base


class ExceptionMatcher(Base):
    """
    expect(lambda: call_something(with_some_params)).to.throw(any_exception)
    """
    @property
    def _raised(self):
        raised = None

        if not callable(self.actual):
            raise TypeError('{actual} is not callable'.format(actual=self.actual))

        try:
            self.actual()
        except BaseException as raised:
            return raised

    def matches(self):
        return isinstance(self._raised, self.expected)

    def failure_message(self):
        if self._raised:
            got = self._raised.__class__.__name__
        else:
            got = 'nothing'

        return 'Expected %s, got %s' % (self.expected.__name__, got)

expect.register('throw', ExceptionMatcher)
