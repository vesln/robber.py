import re


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


def build_called_params_string(call_args):
    match = re.search('call\((.*)\)', str(call_args))
    params = match.group(1)
    return params or 'no arguments'


def unicode_to_str(obj):
    try:
        if type(obj) is unicode:
            return _unicode_string_to_str(obj)
    except NameError:
        pass

    if type(obj) is list:
        return _unicode_list_to_str_list(obj)

    if type(obj) is dict:
        return _unicode_dict_to_str_dict(obj)

    return obj


def _unicode_string_to_str(u_string):
    return u_string.encode('utf-8')


def _unicode_list_to_str_list(u_list):
    str_list = list(u_list)

    for i in range(0, len(str_list)):
        str_list[i] = unicode_to_str(str_list[i])

    return str_list


def _unicode_dict_to_str_dict(u_dict):
    str_dict = dict(u_dict)

    for key in str_dict:
        str_dict[key] = unicode_to_str(str_dict[key])

    return str_dict