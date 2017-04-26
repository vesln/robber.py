from mock import call

from robber import expect
from robber.explanation import Explanation
from robber.helper import Helper
from robber.matchers.base import Base


class CalledWith(Base):
    """
    expect(mock).to.be.called_with(*args, **kwargs)
    """

    def matches(self):
        try:
            return self.actual.called and self.actual.call_args == call(self.expected, *self.args, **self.kwargs)
        except AttributeError:
            raise TypeError('{actual} is not a mock'.format(actual=self.actual))

    @property
    def explanation(self):
        expected_args = Helper.build_expected_params_string(
            expected=self.expected, args=self.args, kwargs=self.kwargs
        )

        if not self.actual.called:
            return Explanation(
                self.actual, self.is_negative, 'be called with', expected_args,
                additional_info='Actually not called', force_disable_repr=True
            )

        called_params = Helper.build_called_params_string(self.actual.call_args)
        return Explanation(
            self.actual, self.is_negative, 'be called with', expected_args,
            called_params, 'Actually called with C', force_disable_repr=True
        )


expect.register('called_with', CalledWith)
