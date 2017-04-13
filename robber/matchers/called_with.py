from mock import call

from robber import expect
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
                        expected_args=self.build_expected_params_string(
                            expected=self.expected, args=self.args, kwargs=self.kwargs
                        )
                    )

        return 'Expected {actual}{negative_message} to be called with {expected_params}. ' \
               'Actually called with {called_params}.'.format(
                    actual=self.actual, negative_message=self.negative_message,
                    expected_params=self.build_expected_params_string(
                        expected=self.expected, args=self.args, kwargs=self.kwargs
                    ),
                    called_params=self.build_called_params_string(self.actual.call_args)
                )

    @staticmethod
    def build_expected_params_string(expected, args, kwargs):
        if not expected:
            expected_params_str = 'no arguments'
        else:
            expected_params_str = str(expected)
            if args:
                # Remove the parenthesis
                args_str = str(args)[1:][:-1]
                expected_params_str = ', '.join((expected_params_str, args_str))

            if kwargs:
                # Convert {'a':  1, 'b': 2} to 'a=1, b=2'
                kwargs_str = ', '.join(['{0}={1!r}'.format(k, v) for k, v in kwargs.items()])
                expected_params_str = ', '.join((expected_params_str, kwargs_str))

        return expected_params_str

    @staticmethod
    def build_called_params_string(call_args):
        if str(call_args) == 'call()':
            called_params_str = 'no arguments'
        else:
            called_params_str = str(call_args)[5:][:-1]

        return called_params_str


expect.register('called_with', CalledWith)
