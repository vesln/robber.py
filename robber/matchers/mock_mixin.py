import re
from mock import call


class MockMixin:
    @property
    def call_args(self):
        if self.expected:
            return call(self.expected, *self.args, **self.kwargs)
        else:
            return call(*self.args, **self.kwargs)

    @property
    def expected_args_str(self):
        if not self.expected and not self.kwargs:
            return 'no arguments'

        expected_args = []

        if self.expected:
            expected_args = [str(self.expected)]

        if self.args:
            # Remove the parenthesis
            match = re.search('\((.*)\)', str(self.args))
            expected_args.append(match.group(1))

        if self.kwargs:
            # Convert {'a':  1, 'b': 2} to 'a=1, b=2'
            kwargs_str = ', '.join(['{0}={1!r}'.format(k, v) for k, v in self.kwargs.items()])

            expected_args.append(kwargs_str)

        return ', '.join(expected_args)

    @property
    def call_args_str(self):
        match = re.search('call\((.*)\)', str(self.actual.call_args))
        params = match.group(1)
        return params or 'no arguments'
