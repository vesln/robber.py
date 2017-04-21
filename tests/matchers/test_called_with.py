from unittest import TestCase

from mock import Mock

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

    def test_failure_message_with_not_called_mock(self):
        mock = Mock()

        called_with = CalledWith(mock, 2)
        message = called_with.failure_message()

        expect(message) == 'Expected {mock} to be called with 2. Actually not called.'.format(mock=mock)

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

        mock(4, 5, 6, c=7)
        called_with = CalledWith(mock, 1, False, 2, 3, a=4)
        message = called_with.failure_message()

        expect(message) == 'Expected {mock} to be called with 1, 2, 3, a=4. ' \
                           'Actually called with 4, 5, 6, c=7.'.format(mock=mock)

    def test_negative_failure_message_with_multiple_args(self):
        mock = Mock()

        mock(1, 2, 3, a=4)
        called_with = CalledWith(mock, 1, True, 2, 3, a=4)
        message = called_with.failure_message()

        expect(message) == 'Expected {mock} not to be called with 1, 2, 3, a=4. ' \
                           'Actually called with 1, 2, 3, a=4.'.format(mock=mock)

    def test_register(self):
        expect(expect.matcher('called_with')) == CalledWith

    def test_not_a_mock(self):
        self.assertRaises(TypeError, CalledWith("a", "b").matches)
        self.assertRaises(TypeError, CalledWith(1, "b").matches)
