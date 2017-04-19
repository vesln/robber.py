from robber import expect
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

    def failure_message(self):
        if self.raised:
            got = self.raised.__class__.__name__
        else:
            got = 'nothing'

        return 'Expected {expected_exception}{negative_message} to be raised, got {actual_exception}'.format(
            expected_exception=self.expected.__name__,
            negative_message=self.negative_message,
            actual_exception=got
        )


expect.register('throw', ExceptionMatcher)
