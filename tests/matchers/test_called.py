from unittest import TestCase

from mock import Mock

from robber import expect
from robber.matchers.called import Called, CalledOnce


class TestCalled(TestCase):
    def test_matches(self):
        mock = Mock()
        mock()
        expect(Called(mock).matches()) == True

    def test_failure_message(self):
        mock = Mock()
        called = Called(mock)
        message = called.failure_message()
        expect(message) == 'Expected {mock} to be called'.format(mock=mock)

    def test_register(self):
        expect(expect.matcher('called')) == Called
        expect(expect.matcher('__called__')) == Called

    def test_not_a_mock(self):
        self.assertRaises(TypeError, Called("a").matches)
        self.assertRaises(TypeError, Called(1).matches)


class TestCalledOnce(TestCase):
    def test_matches(self):
        mock = Mock()
        mock()
        expect(CalledOnce(mock).matches()) == True

    def test_failure_message(self):
        mock = Mock()
        called_once = CalledOnce(mock)
        message = called_once.failure_message()
        expect(message) == 'Expected {mock} to be called once'.format(mock=mock)

    def test_register(self):
        expect(expect.matcher('called_once')) == CalledOnce
        expect(expect.matcher('__called_once__')) == CalledOnce

    def test_not_a_mock(self):
        self.assertRaises(TypeError, CalledOnce("a").matches)
        self.assertRaises(TypeError, CalledOnce(1).matches)
