from difflib import Differ


class Explanation:
    """
    This class gives use a simple way to implement explanations for your expectations.
    """

    def __init__(
            self, a, is_negative, action, b=None, additional_action=None, c=None,
            additional_info=None, negative_action=None, force_disable_repr=False,
            need_to_build_diffs=False, z=None
    ):
        """
        :param a: first object
        :param is_negative: is this a negative explanation?
        :param action: a string defining an action, ex: "equal", "be True", "called"...
        :param b: second object
        :param c: third object
        :param additional_info: custom message that will be put right after the expectation sentence
        :param negative_action: the action used in negative explanation, ex: "be False", "exclude"...
        :param additional_action: the action applied on the third object
        :param force_disable_repr: force disable the use of repr()
        :param need_to_build_diffs: trigger if you want to build the diffs string
        :param z: additional object ex: Expected A to be called with B but actually called with Z
        """

        self.a = a
        self.action = action
        self.b = b
        self.c = c
        self.z = z if not is_negative else None
        self.force_disable_repr = force_disable_repr
        self.need_to_build_diffs = need_to_build_diffs
        self.is_negative = is_negative

        self.action = negative_action if is_negative and negative_action else action
        self.negative_word = ' not' if is_negative and not negative_action else ''
        self.additional_action = ' {0}'.format(additional_action) if additional_action else ''
        self.diffs = self.build_diff(self.a, self.b) if self.need_to_build_diffs else ''
        self.additional_info = self.build_additional_info(additional_info)

        self.b_word = ' B' if b is not None else ''
        self.c_word = ' C' if c is not None else ''
        self.z_word = ' Z' if z is not None else ''

    def build_additional_info(self, info):
        if info:
            if self.is_negative:
                return 'But it happened\n'
            else:
                return '{0}\n'.format(info)
        else:
            return ''

    @property
    def is_repr(self):
        having_two_strings = True if type(self.a) is str and type(self.b) is str else False
        return False if self.force_disable_repr else not having_two_strings

    @property
    def message(self):
        return (
            '\n'
            '{line_a}'
            '{line_b}'
            '{line_c}'
            '{line_z}'
            'Expected A{negative_word} to {action}{b_word}{additional_action}{c_word}\n'
            '{additional_info}'
            '{diffs}'
        ).format(
            line_a=self.build_line(self.a, 'A', self.is_repr, allowed_none=True),
            line_b=self.build_line(self.b, 'B', self.is_repr),
            line_c=self.build_line(self.c, 'C', self.is_repr),
            line_z=self.build_line(self.z, 'Z', self.is_repr),
            negative_word=self.negative_word,
            action=self.action,
            b_word=self.b_word,
            additional_info=self.additional_info,
            additional_action=self.additional_action,
            c_word=self.c_word,
            diffs=self.diffs
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

        return 'Diffs:\n{0}'.format('\n'.join(diffs))
