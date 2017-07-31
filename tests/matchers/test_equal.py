# -*- coding: utf-8 -*-

import sys
from unittest import TestCase

from mock import patch, PropertyMock

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
        expect(equal.dict_diffs).to.eq("""Diffs:
A['b'] = 2
B['b'] = 3
""")


class TestListDiff:
    def test_list_diffs_with_different_length(self):
        l1 = [1]
        d2 = [1, 2]
        equal = Equal(l1, d2)
        expect(equal.list_diffs).to.eq('A and B do not have the same length')

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


class TestStandardizeArgs(TestCase):
    def test_if_unicode_string_is_converted_to_str(self):
        equal = Equal(u'Mèo', u'Mèo')
        equal.matches()
        self.assertEqual(equal.actual, 'Mèo')
        self.assertEqual(equal.expected, 'Mèo')

    def test_if_unicode_list_is_converted_to_str_list(self):
        equal = Equal([u'Mèo', u'Chó'], [u'Mèo', u'Chó'])
        equal.matches()
        self.assertEqual(equal.actual, ['Mèo', 'Chó'])
        self.assertEqual(equal.expected, ['Mèo', 'Chó'])

    def test_if_unicode_dict_is_converted_to_str_dict(self):
        u_dict = {
            'cat': u'Mèo',
            'dog': u'Chó',
        }
        str_dict = {
            'cat': 'Mèo',
            'dog': 'Chó',
        }
        equal = Equal(u_dict, u_dict)
        equal.matches()
        self.assertEqual(equal.actual, str_dict)
        self.assertEqual(equal.expected, str_dict)


class TestUnicodeStringToStr(TestCase):
    def test_unicode_string_to_str(self):
        self.assertEqual(Equal._unicode_string_to_str(u'Mèo'), u'Mèo'.encode('utf-8'))


class TestUnicodeListToStrList(TestCase):
    @patch('robber.matchers.equal.Equal.unicode_to_str')
    def test_unicode_list_to_str_list(self, mock_unicode_to_str):
        Equal._unicode_list_to_str_list([u'Mèo', u'Chó'])
        mock_unicode_to_str.assert_any_call(u'Mèo')
        mock_unicode_to_str.assert_any_call(u'Chó')


class TestUnicodeDictToStrDict(TestCase):
    @patch('robber.matchers.equal.Equal.unicode_to_str')
    def test_unicode_dict_to_str_dict(self, mock_unicode_to_str):
        u_dict = {
            'cat': u'Mèo',
            'dog': u'Chó',
        }

        Equal._unicode_dict_to_str_dict(u_dict)

        mock_unicode_to_str.assert_any_call(u'Mèo')
        mock_unicode_to_str.assert_any_call(u'Chó')


class TestUnicodeToStr(TestCase):
    @patch('robber.matchers.equal.Equal._unicode_string_to_str')
    def test_with_unicode_string(self, mock_unicode_string_to_str):
        Equal.unicode_to_str(u'Mèo')
        # python <= 2.7
        if sys.version_info[0] < 3:
            mock_unicode_string_to_str.assert_called_with(u'Mèo')
        else:
            mock_unicode_string_to_str.assert_not_called()

    @patch('robber.matchers.equal.Equal._unicode_list_to_str_list')
    def test_with_unicode_list(self, mock_unicode_list_to_str_list):
        Equal.unicode_to_str([u'Mèo', u'Chó'])
        mock_unicode_list_to_str_list.assert_called_with([u'Mèo', u'Chó'])

    @patch('robber.matchers.equal.Equal._unicode_dict_to_str_dict')
    def test_with_unicode_dict(self, mock_unicode_dict_to_str_dict):
        u_dict = {
            'cat': u'Mèo',
            'dog': u'Chó',
        }
        Equal.unicode_to_str(u_dict)
        mock_unicode_dict_to_str_dict.assert_called_with(u_dict)
