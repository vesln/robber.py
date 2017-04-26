from difflib import Differ


class Explanation:
    def __init__(
            self, a, is_negative, action, b=None, c=None,
            additional_info=None, negative_action=None, additional_action=None, force_disable_repr=False,
    ):
        self.a = a
        self.action = action
        self.b = b
        self.c = c
        self.force_disable_repr = force_disable_repr

        self.action = negative_action if is_negative and negative_action else action
        self.additional_info = '{0}\n'.format(additional_info) if additional_info else ''
        self.negative_word = ' not' if is_negative and not negative_action else ''
        self.additional_action = ' {0}'.format(additional_action) if additional_action else ''

        self.b_word = ' B' if b is not None else ''
        self.c_word = ' C' if c is not None and additional_action else ''

        self.special_init()

    @property
    def is_repr(self):
        having_two_strings = True if type(self.a) is str and type(self.b) is str else False
        return False if self.force_disable_repr else not having_two_strings

    def special_init(self):
        if self.action == 'equal':
            self.additional_info = self.build_diff(self.a, self.b)

    @property
    def message(self):
        return (
            '\n'
            '{line_a}'
            '{line_b}'
            '{line_c}'
            'Expected A{negative_word} to {action}{b_word}{additional_action}{c_word}\n'
            '{additional_info}'
        ).format(
            line_a=self.build_line(self.a, 'A', self.is_repr, allowed_none=True),
            line_b=self.build_line(self.b, 'B', self.is_repr),
            line_c=self.build_line(self.c, 'C', self.is_repr),
            negative_word=self.negative_word,
            action=self.action,
            b_word=self.b_word,
            additional_info=self.additional_info,
            additional_action=self.additional_action,
            c_word=self.c_word,
        )

    @staticmethod
    def build_line(obj, obj_name, is_repr, allowed_none=False):
        if obj is not None or allowed_none:
            if is_repr:
                obj = repr(obj)
            return '{obj_name} = {obj}\n'.format(
                obj_name=obj_name,
                obj=obj
            )
        return ''

    @staticmethod
    def build_diff(a, b):
        if type(a) is not str or type(b) is not str:
            return ''
        if a == b:
            return ''

        differ = Differ()
        diffs = differ.compare(a.splitlines(), b.splitlines())

        return '\n'.join(diffs)
