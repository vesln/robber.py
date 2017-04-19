from unittest import TestCase

from robber import expect
from robber.explanation import Explanation


class TestExplanation(TestCase):
    def test_init(self):
        explanation = Explanation(1, True, 'called with', 2, 3, 'Actually called with C.')

        expect(explanation.a).to.eq(1)
        expect(explanation.action).to.eq('called with')
        expect(explanation.b).to.eq(2)
        expect(explanation.c).to.eq(3)

    def test_additional_info(self):
        explanation_with_additional_info = Explanation(1, True, 'called with', 2, 3, 'Actually called with C.')
        explanation_without_additional_info = Explanation(1, True, 'called with', 2, 3)

        expect(explanation_with_additional_info.additional_info).to.eq('Actually called with C.\n')
        expect(explanation_without_additional_info.additional_info).to.eq('')

    def test_negative_word(self):
        negative_explanation = Explanation(1, True, 'be truthy')
        positive_explanation = Explanation(1, False, 'be truthy')

        expect(negative_explanation.negative_word).to.eq(' not')
        expect(positive_explanation.negative_word).to.eq('')

    def test_b_word(self):
        explanation_without_b = Explanation(1, True, 'be truthy')
        explanation_with_b = Explanation(1, True, 'equal', 2)

        expect(explanation_without_b.b_word).to.eq('')
        expect(explanation_with_b.b_word).to.eq(' B')

    def test_build_line(self):
        line_with_int = Explanation.build_line(1, 'A')
        line_with_str = Explanation.build_line('1', 'A')
        line_with_empty_str = Explanation.build_line('', 'A')
        line_with_none = Explanation.build_line(None, 'A')

        expect(line_with_int).to.eq('A = 1\n')
        expect(line_with_str).to.eq("A = '1'\n")
        expect(line_with_empty_str).to.eq("A = ''\n")
        expect(line_with_none).to.eq('')

    def test_message(self):
        explanation_with_a = Explanation(1, False, 'be truthy')
        negative_explanation_with_a = Explanation(1, True, 'be truthy')
        explanation_with_a_b = Explanation(1, False, 'equal', 2)
        explanation_with_a_b_c = Explanation('mock', False, 'be called with', 1, 2, 'Actually called with C')

        expect(explanation_with_a.message).to.eq("""
A = 1
Expected A to be truthy
""")
        expect(negative_explanation_with_a.message).to.eq("""
A = 1
Expected A not to be truthy
""")
        expect(explanation_with_a_b.message).to.eq("""
A = 1
B = 2
Expected A to equal B
""")
        expect(explanation_with_a_b_c.message).to.eq("""
A = 'mock'
B = 1
C = 2
Expected A to be called with B
Actually called with C
""")
