from mock import call

from robber import expect
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

    def failure_message(self):
        if not self.actual.called:
            return 'Expected {actual}{negative_message} to be called once with {expected_args}. ' \
                   'Actually not called.'.format(
                        actual=self.actual, negative_message=self.negative_message,
                        expected_args=Helper.build_expected_params_string(
                            expected=self.expected, args=self.args, kwargs=self.kwargs
                        )
                    )

        return 'Expected {actual}{negative_message} to be called once with {expected_params}. ' \
               'Actually called {call_count} times with {called_params}.'.format(
                    actual=self.actual, negative_message=self.negative_message,
                    expected_params=Helper.build_expected_params_string(
                        expected=self.expected, args=self.args, kwargs=self.kwargs
                    ),
                    call_count=self.actual.call_count,
                    called_params=Helper.build_called_params_string(self.actual.call_args)
                )


expect.register('called_once_with', CalledOnceWith)
