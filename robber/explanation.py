import re

from robber.constants import TENSE_WORDS


class Explanation:
    """
    This class gives use a simple way to implement explanations for your expectations.
    """

    def __init__(
            self, actual=object, is_negative=False, action=None, expected=object,
            another_action=None, another_expected=object, more_detail=None, negative_action=None,
            force_disable_repr=False, need_to_build_diffs=False, other=object
    ):
        """
        :param actual: first object
        :param is_negative: is this a negative explanation?
        :param action: a string defining an action, ex: "equal", "be True", "called"...
        :param expected: second object
        :param another_expected: third object
        :param more_detail: custom message that will be put right after the expectation sentence
        :param negative_action: the action used in negative explanation, ex: "be False", "exclude"...
        :param another_action: the action applied on the third object
        :param force_disable_repr: force disable the use of repr()
        :param need_to_build_diffs: trigger if you want to build the diffs string
        :param other: additional object ex: Expected A to be called with B but actually called with Z
        """

        self.actual = actual
        self.action = action
        self.expected = expected
        self.another_expected = another_expected
        self.other = other
        self.force_disable_repr = force_disable_repr
        self.is_negative = is_negative

        self.action = negative_action if is_negative and negative_action else action
        self.negative_word = ' not' if is_negative and not negative_action else ''
        self.another_action = ' {0}'.format(another_action) if another_action else ''
        self.more_detail = self.build_more_detail(more_detail)

        self.expected_word = ' B' if self.is_passed(expected) else ''
        self.another_expected_word = ' C' if self.is_passed(another_expected) else ''
        self.other_word = ' Z' if self.is_passed(other) else ''

    def build_more_detail(self, info):
        if not self.is_passed(self.other) and not info:
            return ''

        if self.is_negative:
            return 'But it happened\n'

        if info:
            return '{0}\n'.format(info)

        if self.is_passed(self.other):
            tense_words_str = ' |'.join(TENSE_WORDS)
            match = re.search('({0}|)(.+)'.format(tense_words_str), self.action)
            other_action = '{action}{another_action} '.format(
                action=match.group(2), another_action=self.another_action
            )
            return 'Actually {0}Z\n'.format(other_action)

    @property
    def is_repr(self):
        having_two_strings = True if type(self.actual) is str and type(self.expected) is str else False
        return False if self.force_disable_repr else not having_two_strings

    @property
    def message(self):
        actual_line = self.build_line(self.actual, 'A', self.is_repr)
        expected_line = self.build_line(self.expected, 'B', self.is_repr)
        another_expected_line = self.build_line(self.another_expected, 'C', self.is_repr)
        other_line = self.build_line(self.other, 'Z', self.is_repr)
        return (
            '\n'
            '{actual_line}'
            '{expected_line}'
            '{another_expected_line}'
            '{other_line}'
            'Expected A{negative_word} to {action}{expected_word}{another_action}{another_expected_word}\n'
            '{more_detail}'
        ).format(
            actual_line=actual_line,
            expected_line=expected_line if self.is_passed(self.expected) else '',
            another_expected_line=another_expected_line if self.is_passed(self.another_expected) else '',
            other_line=other_line if not self.is_negative and self.is_passed(self.other) else '',
            negative_word=self.negative_word,
            action=self.action,
            expected_word=self.expected_word,
            more_detail=self.more_detail,
            another_action=self.another_action,
            another_expected_word=self.another_expected_word,
        )

    @staticmethod
    def build_line(obj, obj_name, is_repr):
        if Explanation.is_passed(obj):
            if is_repr:
                obj = repr(obj)
            return '{obj_name} = {obj}\n'.format(
                obj_name=obj_name,
                obj=obj
            )
        return ''

    @staticmethod
    def is_passed(param):
        return False if param is object else True
