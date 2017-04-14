from unittest import TestCase

from mock import Mock

from robber import expect
from robber.matchers.called_once_with import CalledOnceWith


class TestCalledOnceWith(TestCase):
    def test_matches_with_multiple_args(self):
        mock = Mock()
        mock(1, 2, 3)
        expect(CalledOnceWith(mock, 1, False, 2, 3).matches()).to.eq(True)

    def test_failure_message_with_not_called_mock(self):
        mock = Mock()

        called_once_with = CalledOnceWith(mock, 2)
        called_once_with.matches()
        message = called_once_with.failure_message()

        expect(message) == 'Expected {mock} to be called once with 2. Actually not called.'.format(mock=mock)

    def test_failure_message_with_called_multiple_times(self):
        mock = Mock()
        mock(1)
        mock(1)

        called_once_with = CalledOnceWith(mock, 2)
        called_once_with.matches()
        message = called_once_with.failure_message()

        expect(message) == 'Expected {mock} to be called once with 2. ' \
                           'Actually called 2 times with 1.'.format(mock=mock)

    def test_failure_message_with_wrong_params(self):
        mock = Mock()

        mock(4, 5, 6, c=7)
        called_once_with = CalledOnceWith(mock, 1, False, 2, 3, a=4)
        called_once_with.matches()
        message = called_once_with.failure_message()

        expect(message) == 'Expected {mock} to be called once with 1, 2, 3, a=4. ' \
                           'Actually called 1 times with 4, 5, 6, c=7.'.format(mock=mock)

    def test_negative_failure_message(self):
        mock = Mock()

        mock(1, 2, 3, a=4)
        called_once_with = CalledOnceWith(mock, 1, True, 2, 3, a=4)
        called_once_with.matches()
        message = called_once_with.failure_message()

        expect(message) == 'Expected {mock} not to be called once with 1, 2, 3, a=4. ' \
                           'Actually called 1 times with 1, 2, 3, a=4.'.format(mock=mock)

    def test_register(self):
        expect(expect.matcher('called_once_with')) == CalledOnceWith

    def test_not_a_mock(self):
        self.assertRaises(TypeError, CalledOnceWith("a", "b").matches)
        self.assertRaises(TypeError, CalledOnceWith(1, "b").matches)
