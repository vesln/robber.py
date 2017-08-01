from unittest import TestCase

from robber import expect
from robber.explanation import Explanation


class TestInit(TestCase):
    def test_init(self):
        explanation = Explanation(1, True, 'within', 2, 'and', 3, force_disable_repr=True)

        expect(explanation.actual).to.eq(1)
        expect(explanation.is_negative).to.eq(True)
        expect(explanation.action).to.eq('within')
        expect(explanation.expected).to.eq(2)
        expect(explanation.another_expected).to.eq(3)
        expect(explanation.force_disable_repr).to.eq(True)


class TestMoreDetail(TestCase):
    def test_additional_info_with_negative_explanation(self):
        explanation = Explanation(1, True, 'called with', 2, other=3, more_detail='Some message')
        expect(explanation.more_detail).to.eq('But it happened\n')

    def test_additional_info_with_pre_defined_more_detail(self):
        explanation = Explanation(1, False, 'called with', 2, other=3, more_detail='Some message')
        expect(explanation.more_detail).to.eq('Some message\n')

    def test_additional_info_with_other(self):
        explanation = Explanation(1, False, 'called with', 2, other=3)
        expect(explanation.more_detail).to.eq('Actually called with Z\n')

    def test_additional_info_with_another_action(self):
        explanation = Explanation('func', False, 'change', 2, 'by', 3, other=4)
        expect(explanation.more_detail).to.eq('Actually change by Z\n')

    def test_none_additional_info(self):
        explanation = Explanation(1, True, 'called with', 2, 3)
        expect(explanation.more_detail).to.eq('')


class TestNegativeWord(TestCase):
    def test_negative_word_of_positive_explanation(self):
        explanation = Explanation(1, False, 'be truthy')
        expect(explanation.negative_word).to.eq('')

    def test_negative_word_of_negative_explanation(self):
        explanation = Explanation(1, True, 'be truthy')
        expect(explanation.negative_word).to.eq(' not')

    def test_negative_word_of_negative_explanation_with_negative_action(self):
        explanation = Explanation(1, True, 'be truthy', negative_action='be falsy')
        expect(explanation.negative_word).to.eq('')


class TestAction(TestCase):
    def test_action_of_positive_explanation(self):
        explanation = Explanation(1, False, 'be truthy')
        expect(explanation.action).to.eq('be truthy')

    def test_action_of_negative_explanation(self):
        explanation = Explanation(1, True, 'be truthy')
        expect(explanation.action).to.eq('be truthy')

    def test_action_of_negative_explanation_with_negative_action(self):
        explanation = Explanation(1, True, 'be truthy', negative_action='be falsy')
        expect(explanation.action).to.eq('be falsy')


class TestExpectedWord(TestCase):
    def test_expected_word(self):
        explanation = Explanation(1, True, 'equal', 2)
        expect(explanation.expected_word).to.eq(' B')

    def test_none_expected_word(self):
        explanation = Explanation(1, True, 'be truthy')
        expect(explanation.expected_word).to.eq('')

    def test_expected_word_with_0(self):
        explanation = Explanation(1, False, 0, 'equal')
        expect(explanation.expected_word).to.eq(' B')

    def test_expected_word_with_none(self):
        explanation = Explanation(1, False, None, 'equal')
        expect(explanation.expected_word).to.eq(' B')


class TestAnotherExpectedWord(TestCase):
    def test_another_expected_word(self):
        explanation = Explanation(1, True, 'within', 2, 'and', 3)
        expect(explanation.another_expected_word).to.eq(' C')

    def test_none_another_expected_word(self):
        explanation = Explanation(1, True, 'be truthy')
        expect(explanation.another_expected_word).to.eq('')

    def test_another_expected_word_with_0(self):
        explanation = Explanation(1, True, 'within', -1, 'and', 0)
        expect(explanation.another_expected_word).to.eq(' C')

    def test_another_expected_word_with_none(self):
        explanation = Explanation(1, True, 'within', -1, 'and', None)
        expect(explanation.another_expected_word).to.eq(' C')


class TestOtherWord(TestCase):
    def test_other_word(self):
        explanation = Explanation('func', False, 'change', 1, another_action='by', another_expected=2, other=3)
        expect(explanation.other_word).to.eq(' Z')

    def test_none_other_word(self):
        explanation = Explanation(1, True, 'be truthy')
        expect(explanation.other_word).to.eq('')

    def test_other_word_with_0(self):
        explanation = Explanation('func', False, 'change', 1, another_action='by', another_expected=2, other=0)
        expect(explanation.other_word).to.eq(' Z')

    def test_another_expected_word_with_none(self):
        explanation = Explanation('func', False, 'change', 1, another_action='by', another_expected=2, other=None)
        expect(explanation.other_word).to.eq(' Z')


class TestIsRepr(TestCase):
    def test_is_repr_with_force_disable_repr(self):
        explanation = Explanation('a', True, 'equal', 'b', force_disable_repr=True)
        expect(explanation.is_repr).to.eq(False)

    def test_is_repr_with_two_strings(self):
        explanation = Explanation('a', True, 'equal', 'b')
        expect(explanation.is_repr).to.eq(False)

    def test_is_repr_with_one_strings(self):
        explanation = Explanation('a', True, 'be True')
        expect(explanation.is_repr).to.eq(True)


class TestBuildLine(TestCase):
    def test_build_line_with_int(self):
        line = Explanation.build_line(1, 'A', is_repr=False)
        expect(line).to.eq('A = 1\n')

    def test_build_line_with_is_repr(self):
        line = Explanation.build_line('a', 'A', is_repr=True)
        expect(line).to.eq("A = 'a'\n")

    def test_build_line_with_empty_str(self):
        line = Explanation.build_line('', 'A', is_repr=False)
        expect(line).to.eq('A = \n')

    def test_build_line_with_none(self):
        line = Explanation.build_line(None, 'A', is_repr=True)
        expect(line).to.eq('A = None\n')


class TestMessage(TestCase):
    def test_message_of_explanation_with_a(self):
        explanation = Explanation(1, False, 'be truthy')
        expect(explanation.message).to.eq("""
A = 1
Expected A to be truthy
""")

    def test_message_of_explanation_with_none(self):
        explanation = Explanation(None, False, 'be truthy')
        expect(explanation.message).to.eq("""
A = None
Expected A to be truthy
""")

    def test_message_of_negative_explanation_with_a(self):
        explanation = Explanation(1, True, 'be truthy')
        expect(explanation.message).to.eq("""
A = 1
Expected A not to be truthy
""")

    def test_message_of_explanation_with_a_b(self):
        explanation = Explanation(1, False, 'equal', 2)
        expect(explanation.message).to.eq("""
A = 1
B = 2
Expected A to equal B
""")

    def test_message_of_explanation_with_a_and_none(self):
        explanation = Explanation(1, False, 'equal', None)
        expect(explanation.message).to.eq("""
A = 1
B = None
Expected A to equal B
""")

    def test_message_of_explanation_with_another_action(self):
        explanation = Explanation(1, False, 'be within', 0, 'and', 2)
        expect(explanation.message).to.eq("""
A = 1
B = 0
C = 2
Expected A to be within B and C
""")

    def test_message_of_explanation_with_other(self):
        explanation = Explanation(
            'func', False, 'change', 1, another_action='by', another_expected=2,
            other=3, force_disable_repr=True
        )
        expect(explanation.message).to.eq("""
A = func
B = 1
C = 2
Z = 3
Expected A to change B by C
Actually change by Z
""")


class TestIsPassed(TestCase):
    def test_is_passed_called_with_object(self):
        expect(Explanation.is_passed(object)).to.eq(False)

    def test_is_passed_called_with_none(self):
        expect(Explanation.is_passed(None)).to.eq(True)

    def test_is_passed_called_with_normal_params(self):
        expect(Explanation.is_passed(1)).to.eq(True)
        expect(Explanation.is_passed('a')).to.eq(True)
