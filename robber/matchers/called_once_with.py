from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base
from robber.matchers.mock_mixin import MockMixin


class CalledOnceWith(Base, MockMixin):
    """
    expect(mock).to.be.called_once_with(*args, **kwargs)
    """

    def matches(self):
        try:
            called_once = self.actual.call_count == 1
            called_with = self.actual.call_args == self.call_args
        except AttributeError:
            raise TypeError('{actual} is not a mock'.format(actual=self.actual))
        else:
            return called_once and called_with

    @property
    def explanation(self):
        if not self.actual.called:
            return Explanation(
                self.actual, self.is_negative, 'be called once with', self.expected_args_str,
                more_detail='Actually not called', force_disable_repr=True
            )

        additional_info = 'Actually called {call_count} times with Z'.format(call_count=self.actual.call_count)

        return Explanation(
            self.actual, self.is_negative, 'be called once with', self.expected_args_str,
            other=self.call_args_str, more_detail=additional_info, force_disable_repr=True
        )


expect.register('called_once_with', CalledOnceWith)
