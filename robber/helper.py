class Helper:
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
