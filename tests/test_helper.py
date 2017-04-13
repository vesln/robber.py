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
