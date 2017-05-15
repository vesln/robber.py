from unittest import TestCase

from mock import patch
from mock.mock import PropertyMock

from robber import expect
from robber.matchers.equal import Equal


class TestEqual:
    def test_matches(self):
        expect(Equal(1, 1).matches()).to.eq(True)
        expect(Equal(1, 2).matches()).to.eq(False)

    def test_register(self):
        expect(expect.matcher('eq')) == Equal
        expect(expect.matcher('__eq__')) == Equal
        expect(expect.matcher('ne')) == Equal
        expect(expect.matcher('__ne__')) == Equal


class TestDictDiff:
    def test_dict_diffs_with_different_length(self):
        d1 = {'a': 1}
        d2 = {'a': 1, 'b': 2}
        equal = Equal(d1, d2)
        expect(equal.dict_diffs).to.eq('A and B does not have the same length')

    def test_dict_diffs_with_different_key(self):
        d1 = {'a': 1, 'c': 2}
        d2 = {'a': 1, 'b': 2}
        equal = Equal(d1, d2)
        expect(equal.dict_diffs).to.eq("A has key 'c' while B does not")

    def test_dict_diffs_with_different_value(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 1, 'b': 3}
        equal = Equal(d1, d2)
        expect(equal.dict_diffs).to.eq("A['b'] = 2 while B['b'] = 3")


class TestExplanationMessage(TestCase):
    def test_positive_explanation_message(self):
        equal = Equal('123', 123)
        message = equal.explanation.message
        expect(message).to.eq("""
A = '123'
B = 123
Expected A to equal B
""")

    def test_negative_explanation_message(self):
        equal = Equal('actual', 'actual', is_negative=True)
        message = equal.explanation.message
        expect(message).to.eq("""
A = actual
B = actual
Expected A not to equal B
""")

    def test_explanation_message_when_compare_two_strings(self):
        string_a = """The walking cats
are walking"""
        string_b = """The walking dogs
are walking"""
        equal = Equal(string_a, string_b, is_negative=False)
        message = equal.explanation.message
        expect(message).to.eq("""
A = The walking cats
are walking
B = The walking dogs
are walking
Expected A to equal B
Diffs:
- The walking cats
?             ^^^

+ The walking dogs
?             ^^^

  are walking""")

    @patch('robber.matchers.equal.Equal.dict_diffs', new_callable=PropertyMock)
    def test_explanation_message_with_two_dicts(self, mock_dict_diffs):
        mock_dict_diffs.return_value = 'Some diffs'
        d1 = {'a': 1, 'c': 2}
        d2 = {'a': 1, 'b': 3}
        equal = Equal(d1, d2)

        expect('Some diffs' in equal.explanation.message).to.eq(True)
