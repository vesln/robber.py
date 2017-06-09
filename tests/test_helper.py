# -*- coding: utf-8 -*-

import sys
from unittest import TestCase

from mock import call

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


class TestIsUnicode(TestCase):
    def test_with_str(self):
        expect(Helper.is_unicode('a')).to.eq(False)

    def test_with_unicode(self):
        # python <= 2.7
        if type(sys.version_info) is tuple or sys.version_info.major < 3:
            expect(Helper.is_unicode(u'a')).to.eq(True)
        else:
            expect(Helper.is_unicode(u'a')).to.eq(False)

    def test_with_int(self):
        expect(Helper.is_unicode(1)).to.eq(False)


class TestIsStrOrUnicode(TestCase):
    def test_with_str(self):
        expect(Helper.is_str_or_unicode('a')).to.eq(True)

    def test_with_unicode(self):
        expect(Helper.is_str_or_unicode(u'a')).to.eq(True)

    def test_with_int(self):
        expect(Helper.is_str_or_unicode(1)).to.eq(False)


class TestUnicodeToStr(TestCase):
    def test_unicode_to_str(self):
        self.assertEqual(Helper.unicode_to_str(u'Mèo'), u'Mèo'.encode('utf-8'))


class TestUnicodeListToStrList(TestCase):
    def test_with_simple_list(self):
        u_list = [u'Mèo', u'Chó']
        str_list = ['Mèo', 'Chó']
        self.assertEqual(Helper.unicode_list_to_str_list(u_list), str_list)

    def test_with_multi_level_list(self):
        u_list = [[u'Mèo'], [u'Chó']]
        str_list = [['Mèo'], ['Chó']]
        self.assertEqual(Helper.unicode_list_to_str_list(u_list), str_list)


class TestUnicodeDictToStrDict(TestCase):
    def test_with_simple_dict(self):
        u_dict = {
            'cat': u'Mèo',
            'dog': u'Chó',
        }
        str_dict = {
            'cat': 'Mèo',
            'dog': 'Chó',
        }
        self.assertEqual(Helper.unicode_dict_to_str_dict(u_dict), str_dict)

    def test_with_multi_level_dict(self):
        u_dict = {
            'd1': {'cat': u'Mèo'},
            'd2': {'dog': u'Chó'},
        }
        str_dict = {
            'd1': {'cat': 'Mèo'},
            'd2': {'dog': 'Chó'},
        }
        self.assertEqual(Helper.unicode_dict_to_str_dict(u_dict), str_dict)
