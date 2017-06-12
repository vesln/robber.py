from mock import call

from robber import expect
from robber.explanation import Explanation
from robber.helper import build_expected_params_string
from robber.matchers.base import Base


class EverCalledWith(Base):
    """
    expect(mock).to.have.been.ever_called_with(*args, **kwargs)
    expect(mock).to.have.any_call(*args, **kwargs)
    """

    def matches(self):
        try:
            return call(self.expected, *self.args, **self.kwargs) in self.actual.call_args_list
        except AttributeError:
            raise TypeError('{actual} is not a mock'.format(actual=self.actual))

    @property
    def explanation(self):
        expected_args = build_expected_params_string(
            expected=self.expected, args=self.args, kwargs=self.kwargs
        )
        return Explanation(
            self.actual, self.is_negative, 'have been ever called with', expected_args,
            force_disable_repr=True
        )


expect.register('ever_called_with', EverCalledWith)
expect.register('any_call', EverCalledWith)
