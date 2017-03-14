from unittest import TestCase

from mock import Mock

from robber import expect
from robber.matchers.called import Called


class TestCalled(TestCase):
    def test_matches(self):
        mock = Mock()
        mock()
        expect(Called(mock).matches()) == True

    def test_failure_message(self):
        mock = Mock()
        called = Called(mock)
        message = called.failure_message()
        expect(message) == 'Expected {function} to be called'.format(function=mock)

    def test_register(self):
        expect(expect.matcher('called')) == Called
        expect(expect.matcher('__called__')) == Called

    def test_not_a_mock(self):
        with self.assertRaises(TypeError):
            expect(Called("a").matches()) == True
        with self.assertRaises(TypeError):
            expect(Called(1).matches()) == True
