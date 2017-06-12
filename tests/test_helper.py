# -*- coding: utf-8 -*-
import sys
from unittest import TestCase

from mock import call, patch

from robber.expect import expect
from robber.helper import Helper


class TestBuildCalledParamsString(TestCase):
    def test_with_no_params(self):
        call_args = call()
        call_args_str = Helper.build_called_params_string(call_args)

        expect(call_args_str).to.eq('no arguments')

    def test_with_args_and_kwargs(self):
        call_args = call(1, 'a', 3, a=1, b=2)
        call_args_str = Helper.build_called_params_string(call_args)

        expect(call_args_str).to.eq("1, 'a', 3, a=1, b=2")


class TestBuildExpectedParamsString(TestCase):
    def test_with_no_params(self):
        expected_params_str = Helper.build_expected_params_string(expected=None, args=None, kwargs=None)
        expect(expected_params_str).to.eq('no arguments')

    def test_with_expected(self):
        expected_params_str = Helper.build_expected_params_string(expected=1, args=None, kwargs=None)
        expect(expected_params_str).to.eq('1')

    def test_with_expected_and_args(self):
        expected_params_str = Helper.build_expected_params_string(expected=1, args=(2, 'a'), kwargs=None)
        expect(expected_params_str).to.eq("1, 2, 'a'")

    def test_with_expected_and_kwargs(self):
        expected_params_str = Helper.build_expected_params_string(
            expected=1, args=None, kwargs={'a': 'a', 'one': 1}
        )
        # Since we cannot be sure about the order of a dict, which leads to the situation that the function
        # build_expected_params_string can return different results (still acceptable). In order to test, we will split
        # the result into smaller parts, and assert each one.
        split_expected_params_str = expected_params_str.split(', ')

        expect(split_expected_params_str).to.contain('1')
        expect(split_expected_params_str).to.contain("a='a'")
        expect(split_expected_params_str).to.contain('one=1')

    def test_with_expected_and_args_and_kwargs(self):
        expected_params_str = Helper.build_expected_params_string(
            expected=1, args=(2, 'a'), kwargs={'b': 'b', 'one': 1}
        )
        split_expected_params_str = expected_params_str.split(', ')

        expect(split_expected_params_str).to.contain('1')
        expect(split_expected_params_str).to.contain('2')
        expect(split_expected_params_str).to.contain("'a'")
        expect(split_expected_params_str).to.contain("b='b'")
        expect(split_expected_params_str).to.contain('one=1')


class TestUnicodeStringToStr(TestCase):
    def test_unicode_string_to_str(self):
        self.assertEqual(Helper.unicode_string_to_str(u'Mèo'), u'Mèo'.encode('utf-8'))


class TestUnicodeListToStrList(TestCase):
    @patch('tests.test_helper.Helper.unicode_to_str')
    def test_unicode_list_to_str_list(self, mock_unicode_to_str):
        Helper.unicode_list_to_str_list([u'Mèo', u'Chó'])
        mock_unicode_to_str.assert_any_call(u'Mèo')
        mock_unicode_to_str.assert_any_call(u'Chó')


class TestUnicodeDictToStrDict(TestCase):
    @patch('tests.test_helper.Helper.unicode_to_str')
    def test_unicode_dict_to_str_dict(self, mock_unicode_to_str):
        u_dict = {
            'cat': u'Mèo',
            'dog': u'Chó',
        }
        Helper.unicode_dict_to_str_dict(u_dict)
        mock_unicode_to_str.assert_any_call(u'Mèo')
        mock_unicode_to_str.assert_any_call(u'Chó')


class TestUnicodeToStr(TestCase):
    @patch('tests.test_helper.Helper.unicode_string_to_str')
    def test_with_unicode_string(self, mock_unicode_string_to_str):
        Helper.unicode_to_str(u'Mèo')
        # python <= 2.7
        if sys.version_info[0] < 3:
            mock_unicode_string_to_str.assert_called_with(u'Mèo')
        else:
            mock_unicode_string_to_str.assert_not_called()

    @patch('tests.test_helper.Helper.unicode_list_to_str_list')
    def test_with_unicode_list(self, mock_unicode_list_to_str_list):
        Helper.unicode_to_str([u'Mèo', u'Chó'])
        mock_unicode_list_to_str_list.assert_called_with([u'Mèo', u'Chó'])

    @patch('tests.test_helper.Helper.unicode_dict_to_str_dict')
    def test_with_unicode_dict(self, mock_unicode_dict_to_str_dict):
        u_dict = {
            'cat': u'Mèo',
            'dog': u'Chó',
        }
        Helper.unicode_to_str(u_dict)
        mock_unicode_dict_to_str_dict.assert_called_with(u_dict)
