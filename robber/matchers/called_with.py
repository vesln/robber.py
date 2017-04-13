from mock import call

from robber import expect
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

    def failure_message(self):
        if not self.actual.called:
            return 'Expected {actual}{negative_message} to be called with {expected_args}. ' \
                   'Actually not called.'.format(
                        actual=self.actual, negative_message=self.negative_message,
                        expected_args=Helper.build_expected_params_string(
                            expected=self.expected, args=self.args, kwargs=self.kwargs
                        )
                    )

        return 'Expected {actual}{negative_message} to be called with {expected_params}. ' \
               'Actually called with {called_params}.'.format(
                    actual=self.actual, negative_message=self.negative_message,
                    expected_params=Helper.build_expected_params_string(
                        expected=self.expected, args=self.args, kwargs=self.kwargs
                    ),
                    called_params=Helper.build_called_params_string(self.actual.call_args)
                )


expect.register('called_with', CalledWith)
