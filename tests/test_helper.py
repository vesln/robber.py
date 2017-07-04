# -*- coding: utf-8 -*-

import sys
from unittest import TestCase

from mock import patch

from robber.helper import _unicode_string_to_str, _unicode_list_to_str_list, unicode_to_str, _unicode_dict_to_str_dict


class TestUnicodeStringToStr(TestCase):
    def test_unicode_string_to_str(self):
        self.assertEqual(_unicode_string_to_str(u'Mèo'), u'Mèo'.encode('utf-8'))


class TestUnicodeListToStrList(TestCase):
    @patch('robber.helper.unicode_to_str')
    def test_unicode_list_to_str_list(self, mock_unicode_to_str):
        _unicode_list_to_str_list([u'Mèo', u'Chó'])
        mock_unicode_to_str.assert_any_call(u'Mèo')
        mock_unicode_to_str.assert_any_call(u'Chó')


class TestUnicodeDictToStrDict(TestCase):
    @patch('robber.helper.unicode_to_str')
    def test_unicode_dict_to_str_dict(self, mock_unicode_to_str):
        u_dict = {
            'cat': u'Mèo',
            'dog': u'Chó',
        }
        _unicode_dict_to_str_dict(u_dict)
        mock_unicode_to_str.assert_any_call(u'Mèo')
        mock_unicode_to_str.assert_any_call(u'Chó')


class TestUnicodeToStr(TestCase):
    @patch('robber.helper._unicode_string_to_str')
    def test_with_unicode_string(self, mock_unicode_string_to_str):
        unicode_to_str(u'Mèo')
        # python <= 2.7
        if sys.version_info[0] < 3:
            mock_unicode_string_to_str.assert_called_with(u'Mèo')
        else:
            mock_unicode_string_to_str.assert_not_called()

    @patch('robber.helper._unicode_list_to_str_list')
    def test_with_unicode_list(self, mock_unicode_list_to_str_list):
        unicode_to_str([u'Mèo', u'Chó'])
        mock_unicode_list_to_str_list.assert_called_with([u'Mèo', u'Chó'])

    @patch('robber.helper._unicode_dict_to_str_dict')
    def test_with_unicode_dict(self, mock_unicode_dict_to_str_dict):
        u_dict = {
            'cat': u'Mèo',
            'dog': u'Chó',
        }
        unicode_to_str(u_dict)
        mock_unicode_dict_to_str_dict.assert_called_with(u_dict)
