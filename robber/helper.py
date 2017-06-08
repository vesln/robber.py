import re


class Helper:
    @staticmethod
    def build_expected_params_string(expected, args, kwargs):
        if not expected:
            return 'no arguments'

        expected_params_str = str(expected)
        if args:
            # Remove the parenthesis
            match = re.search('\((.*)\)', str(args))
            args_str = match.group(1)
            expected_params_str = ', '.join((expected_params_str, args_str))

        if kwargs:
            # Convert {'a':  1, 'b': 2} to 'a=1, b=2'
            kwargs_str = ', '.join(['{0}={1!r}'.format(k, v) for k, v in kwargs.items()])
            expected_params_str = ', '.join((expected_params_str, kwargs_str))

        return expected_params_str

    @staticmethod
    def build_called_params_string(call_args):
        match = re.search('call\((.*)\)', str(call_args))
        params = match.group(1)
        return params or 'no arguments'

    @classmethod
    def is_str_or_unicode(cls, obj):
        return type(obj) is str or cls.is_unicode(obj)

    @staticmethod
    def is_unicode(obj):
        try:
            return type(obj) is unicode
        except NameError:
            return False

    @staticmethod
    def unicode_to_str(u_string):
        return u_string.encode('utf-8')
