from unittest import TestCase

from mock import Mock, call

from robber import expect
from robber.matchers.called_with import CalledWith


class TestCalledWith(TestCase):
    def test_matches_with_one_arg(self):
        mock = Mock()
        mock('a')
        expect(CalledWith(mock, 'a').matches()).to.eq(True)

    def test_matches_with_multiple_args(self):
        mock = Mock()
        mock(1, 2, 3)
        expect(CalledWith(mock, 1, False, 2, 3).matches()).to.eq(True)

    def test_failure_message_with_one_arg(self):
        mock = Mock()
        mock(1)

        called_with = CalledWith(mock, 2)
        message = called_with.failure_message()

        expect(message) == 'Expected {mock} to be called with 2. Actually called with 1.'.format(mock=mock)

    def test_negative_failure_message_with_one_arg(self):
        mock = Mock()
        mock(2)

        called_with = CalledWith(mock, 2, is_negative=True)
        message = called_with.failure_message()

        expect(message) == 'Expected {mock} not to be called with 2. Actually called with 2.'.format(mock=mock)

    def test_failure_message_with_multiple_args(self):
        mock = Mock()

        mock(4, 5, 6, c=7, d=8)
        called_with = CalledWith(mock, 1, False, 2, 3, a=4, b=5)
        message = called_with.failure_message()

        expect(message) == 'Expected {mock} to be called with 1, 2, 3, a=4, b=5. ' \
                           'Actually called with 4, 5, 6, c=7, d=8.'.format(mock=mock)

    def test_negative_failure_message_with_multiple_args(self):
        mock = Mock()

        mock(1, 2, 3, a=4, b=5)
        called_with = CalledWith(mock, 1, True, 2, 3, a=4, b=5)
        message = called_with.failure_message()

        expect(message) == 'Expected {mock} not to be called with 1, 2, 3, a=4, b=5. ' \
                           'Actually called with 1, 2, 3, a=4, b=5.'.format(mock=mock)

    def test_register(self):
        expect(expect.matcher('called_with')) == CalledWith

    def test_not_a_mock(self):
        self.assertRaises(TypeError, CalledWith("a", "b").matches)
        self.assertRaises(TypeError, CalledWith(1, "b").matches)


class TestBuildCalledParamsString(TestCase):
    def test_with_no_params(self):
        call_args = call()
        call_args_str = CalledWith.build_called_params_string(call_args)

        expect(call_args_str).to.eq('no arguments')

    def test_with_args_and_kwargs(self):
        call_args = call(1, 'a', 3, a=1, b=2)
        call_args_str = CalledWith.build_called_params_string(call_args)

        expect(call_args_str).to.eq("1, 'a', 3, a=1, b=2")


class TestBuildExpectedParamsString(TestCase):
    def test_with_no_params(self):
        expected_params_str = CalledWith.build_expected_params_string(expected=None, args=None, kwargs=None)
        expect(expected_params_str).to.eq('no arguments')

    def test_with_expected(self):
        expected_params_str = CalledWith.build_expected_params_string(expected=1, args=None, kwargs=None)
        expect(expected_params_str).to.eq('1')

    def test_with_expected_and_args(self):
        expected_params_str = CalledWith.build_expected_params_string(expected=1, args=(2, 'a'), kwargs=None)
        expect(expected_params_str).to.eq("1, 2, 'a'")

    def test_with_expected_and_kwargs(self):
        expected_params_str = CalledWith.build_expected_params_string(
            expected=1, args=None, kwargs={'one': 1, 'b': 'b'}
        )
        expect(expected_params_str).to.eq("1, one=1, b='b'")

    def test_with_expected_and_args_and_kwargs(self):
        expected_params_str = CalledWith.build_expected_params_string(
            expected=1, args=(2, 'a'), kwargs={'one': 1, 'b': 'b'}
        )
        expect(expected_params_str).to.eq("1, 2, 'a', one=1, b='b'")
