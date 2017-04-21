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


class TestHavingTwoStrings(TestCase):
    def test_having_two_strings_with_two_strings(self):
        explanation = Explanation('a', True, 'equal', 'b')
        expect(explanation.having_two_strings).to.eq(True)

    def test_having_two_strings_with_one_strings(self):
        explanation = Explanation('a', True, 'equal', 2)
        expect(explanation.having_two_strings).to.eq(False)

    def test_having_two_strings_with_no_strings(self):
        explanation = Explanation(1, True, 'equal', 2)
        expect(explanation.having_two_strings).to.eq(False)


class TestSpecialInit(TestCase):
    @patch('tests.test_explanation.Explanation.build_diff')
    def test_special_init_with_equal(self, mock_build_diff):
        Explanation('a', True, 'equal', 'b')
        mock_build_diff.assert_called_with('a', 'b')

    @patch('tests.test_explanation.Explanation.build_diff')
    def test_special_init_with_other_than_equal(self, mock_build_diff):
        Explanation('a', True, 'something', 'b')
        mock_build_diff.assert_not_called()


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
