from unittest import TestCase

from mock import patch

from robber import expect
from robber.explanation import Explanation


class TestInit(TestCase):
    def test_init(self):
        explanation = Explanation(1, True, 'called with', 2, 3, 'Actually called with C.')

        expect(explanation.a).to.eq(1)
        expect(explanation.action).to.eq('called with')
        expect(explanation.b).to.eq(2)
        expect(explanation.c).to.eq(3)


class TestAdditionalInfo(TestCase):
    def test_additional_info(self):
        explanation = Explanation(1, True, 'called with', 2, 3, 'Actually called with C.')
        expect(explanation.additional_info).to.eq('Actually called with C.\n')

    def test_none_additional_info(self):
        explanation = Explanation(1, True, 'called with', 2, 3)
        expect(explanation.additional_info).to.eq('')


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


class TestBWord(TestCase):
    def test_b_word(self):
        explanation = Explanation(1, True, 'equal', 2)
        expect(explanation.b_word).to.eq(' B')

    def test_none_b_word(self):
        explanation = Explanation(1, True, 'be truthy')
        expect(explanation.b_word).to.eq('')

    def test_b_word_with_0(self):
        explanation = Explanation(1, False, 0, 'equal')
        expect(explanation.b_word).to.eq(' B')


class TestCWord(TestCase):
    def test_c_word(self):
        explanation = Explanation(1, True, 'within', 2, 3, additional_action='and')
        expect(explanation.c_word).to.eq(' C')

    def test_c_word_without_additional_action(self):
        explanation = Explanation('mock', False, 'be called with', 1, 2, 'Actually called with C')
        expect(explanation.c_word).to.eq('')

    def test_none_c_word(self):
        explanation = Explanation(1, True, 'be truthy')
        expect(explanation.c_word).to.eq('')

    def test_c_word_with_0(self):
        explanation = Explanation(1, True, 'within', -1, 0, additional_action='and')
        expect(explanation.c_word).to.eq(' C')


class TestDiffs(TestCase):
    @patch('tests.test_explanation.Explanation.build_diff')
    def test_diffs_with_need_to_build_diffs(self, mock_build_diff):
        mock_build_diff.return_value = 'diffs'
        explanation = Explanation('a', False, 'equal', 'b', need_to_build_diffs=True)
        expect(explanation.diffs).to.eq('diffs')

    @patch('tests.test_explanation.Explanation.build_diff')
    def test_diffs_with_no_need_to_build_diffs(self, mock_build_diff):
        mock_build_diff.return_value = 'diffs'
        explanation = Explanation('a', False, 'equal', 'b')
        expect(explanation.diffs).to.eq('')


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
        expect(line).to.eq('')

    def test_build_line_allowed_none(self):
        line = Explanation.build_line(None, 'A', is_repr=True, allowed_none=True)
        expect(line).to.eq('A = None\n')


class TestBuildDiff(TestCase):
    def test_build_diff_with_no_strings(self):
        diff = Explanation.build_diff(2, 1)
        expect(diff).to.eq('')

    def test_build_diff_with_one_string(self):
        diff = Explanation.build_diff('a', 1)
        expect(diff).to.eq('')

    def test_build_diff_with_two_equal_strings(self):
        diff = Explanation.build_diff('a', 'a')
        expect(diff).to.eq('')

    def test_build_diff_with_two_not_equal_strings(self):
        diff = Explanation.build_diff('A little cat', 'A little dog')
        expect(diff).to.eq("""- A little cat
?          ^^^

+ A little dog
?          ^^^
""")


class TestMessage(TestCase):
    def test_message_of_explanation_with_a(self):
        explanation = Explanation(1, False, 'be truthy')
        expect(explanation.message).to.eq("""
A = 1
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

    def test_message_of_explanation_with_a_b_c(self):
        explanation = Explanation('mock', False, 'be called with', 1, 2, 'Actually called with C')
        expect(explanation.message).to.eq("""
A = 'mock'
B = 1
C = 2
Expected A to be called with B
Actually called with C
""")

    def test_message_of_explanation_with_a_b_c_and_additional_action(self):
        explanation = Explanation(1, False, 'be within', 0, 2, additional_action='and')
        expect(explanation.message).to.eq("""
A = 1
B = 0
C = 2
Expected A to be within B and C
""")
