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

    @classmethod
    def unicode_list_to_str_list(cls, u_list):
        str_list = list(u_list)

        for i in range(0, len(str_list)):
            if cls.is_unicode(str_list[i]):
                str_list[i] = cls.unicode_to_str(str_list[i])
            elif type(str_list[i]) is list:
                str_list[i] = cls.unicode_list_to_str_list(str_list[i])

        return str_list

    @classmethod
    def unicode_dict_to_str_dict(cls, u_dict):
        str_dict = dict(u_dict)

        for key in str_dict:
            if cls.is_unicode(str_dict[key]):
                str_dict[key] = cls.unicode_to_str(str_dict[key])
            elif type(str_dict[key]) is dict:
                str_dict[key] = cls.unicode_dict_to_str_dict(str_dict[key])

        return str_dict
