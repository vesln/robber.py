from unittest import TestCase

from mock import Mock

from robber import expect
from robber.matchers.called_with import CalledWith


class TestCalledWith(TestCase):
    def test_matches(self):
        mock = Mock()
        mock('a')
        # expect(CalledWith(mock, 'a').matches()) is True
        expect(CalledWith(mock, 'b').matches()) is True

    def test_failure_message(self):
        mock = Mock()
        called_with = CalledWith(mock, 'a')
        message = called_with.failure_message()
        expect(message) == 'Expected {mock} to be called with a'.format(mock=mock)

    def test_register(self):
        expect(expect.matcher('called_with')) == CalledWith
        expect(expect.matcher('__called_with__')) == CalledWith

    def test_not_a_mock(self):
        self.assertRaises(TypeError, CalledWith("a", "b").matches)
        self.assertRaises(TypeError, CalledWith(1, "b").matches)
