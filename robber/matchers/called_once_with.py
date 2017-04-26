from mock import call

from robber import expect
from robber.explanation import Explanation
from robber.helper import Helper
from robber.matchers.base import Base


class CalledOnceWith(Base):
    """
    expect(mock).to.be.called_once_with(*args, **kwargs)
    """

    def matches(self):
        try:
            called_once = self.actual.call_count == 1
            called_with = self.actual.call_args == call(self.expected, *self.args, **self.kwargs)
            return called_once and called_with
        except AttributeError:
            raise TypeError('{actual} is not a mock'.format(actual=self.actual))

    @property
    def explanation(self):
        expected_args = Helper.build_expected_params_string(
            expected=self.expected, args=self.args, kwargs=self.kwargs
        )

        if not self.actual.called:
            return Explanation(
                self.actual, self.is_negative, 'be called once with', expected_args,
                additional_info='Actually not called', force_disable_repr=True
            )

        called_args = Helper.build_called_params_string(self.actual.call_args)
        additional_info = 'Actually called {call_count} times with C'.format(call_count=self.actual.call_count)

        return Explanation(
            self.actual, self.is_negative, 'be called once with', expected_args, called_args,
            additional_info=additional_info, force_disable_repr=True
        )


expect.register('called_once_with', CalledOnceWith)
