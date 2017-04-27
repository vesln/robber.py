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
    def explanation(self):
        if self.raised:
            got = self.raised.__class__.__name__
        else:
            got = 'nothing'

        return Explanation(
            self.expected.__name__, self.is_negative, 'be raised',
            z=got, additional_info='Actually got Z'
        )


expect.register('throw', ExceptionMatcher)
