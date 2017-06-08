# -*- coding: utf-8 -*-

from unittest import TestCase

from mock import patch
from mock.mock import PropertyMock

from robber import expect
from robber.matchers.equal import Equal


class TestEqual:
    def test_matches(self):
        expect(Equal(1, 1).matches()).to.eq(True)
        expect(Equal(1, 2).matches()).to.eq(False)

    def test_if_unicode_string_is_converted_to_str(self):
        equal = Equal(u'Mèo', u'Mèo')
        equal.matches()
        expect(type(equal.actual)).to.equal(str)
        expect(type(equal.expected)).to.equal(str)

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


class TestListDiff:
    def test_list_diffs_with_different_length(self):
        l1 = [1]
        d2 = [1, 2]
        equal = Equal(l1, d2)
        expect(equal.list_diffs).to.eq('A and B does not have the same length')

    def test_list_diffs_with_different_member(self):
        l1 = [1, 2]
        d2 = [1, 3]
        equal = Equal(l1, d2)
        expect(equal.list_diffs).to.eq("A contains 2 while B does not")


class TestStrDiff(TestCase):
    def test_str_diff_with_two_equal_strings(self):
        equal = Equal('a', 'a', is_negative=True)
        expect(equal.str_diffs).to.eq('')

    def test_str_diff_with_strings(self):
        equal = Equal('A little cat', 'A little dog', is_negative=False)
        expect(equal.str_diffs).to.eq("""Diffs:
- A little cat
?          ^^^

+ A little dog
?          ^^^
""")


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

    @patch('robber.matchers.equal.Equal.dict_diffs', new_callable=PropertyMock)
    def test_explanation_message_with_two_dicts(self, mock_dict_diffs):
        mock_dict_diffs.return_value = 'Some diffs'
        d1 = {'a': 1, 'c': 2}
        d2 = {'a': 1, 'b': 3}
        equal = Equal(d1, d2)

        expect('Some diffs' in equal.explanation.message).to.eq(True)

    @patch('robber.matchers.equal.Equal.list_diffs', new_callable=PropertyMock)
    def test_explanation_message_with_two_lists(self, mock_list_diffs):
        mock_list_diffs.return_value = 'Some diffs'
        l1 = [1, 2]
        l2 = [1, 3]
        equal = Equal(l1, l2)

        expect('Some diffs' in equal.explanation.message).to.eq(True)

    @patch('robber.matchers.equal.Equal.str_diffs', new_callable=PropertyMock)
    def test_explanation_message_with_two_strings(self, mock_str_diffs):
        mock_str_diffs.return_value = 'Some diffs'
        l1 = 'cat'
        l2 = 'dog'
        equal = Equal(l1, l2)

        expect('Some diffs' in equal.explanation.message).to.eq(True)
