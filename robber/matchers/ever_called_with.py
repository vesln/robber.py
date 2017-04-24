from mock import call

from robber import expect
from robber.helper import Helper
from robber.matchers.base import Base


class EverCalledWith(Base):
    """
    expect(mock).to.have.been.ever_called_with(*args, **kwargs)
    """

    def matches(self):
        try:
            return call(self.expected, *self.args, **self.kwargs) in self.actual.call_args_list
        except AttributeError:
            raise TypeError('{actual} is not a mock'.format(actual=self.actual))

    def failure_message(self):
        return 'Expected {actual}{negative_message} to have been ever called with {expected_args}.'.format(
            actual=self.actual, negative_message=self.negative_message,
            expected_args=Helper.build_expected_params_string(
                expected=self.expected, args=self.args, kwargs=self.kwargs
            )
        )


expect.register('ever_called_with', EverCalledWith)
