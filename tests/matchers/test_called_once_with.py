from unittest import TestCase

from mock import Mock

from robber import expect
from robber.matchers.called_once_with import CalledOnceWith


class TestCalledOnceWith(TestCase):
    def test_matches(self):
        mock = Mock()
        mock(1, 2, 3, a=4)
        expect(CalledOnceWith(mock, 1, False, 2, 3, a=4).matches()).to.eq(True)

    def test_failure_message_with_not_called_mock(self):
        mock = Mock()

        called_once_with = CalledOnceWith(mock, 2)
        called_once_with.matches()
        message = called_once_with.explanation.message

        expect(message) == """
A = {0}
B = 2
Expected A to be called once with B
Actually not called
""".format(mock)

    def test_failure_message_with_called_multiple_times(self):
        mock = Mock()
        mock(1)
        mock(1)

        called_once_with = CalledOnceWith(mock, 2)
        called_once_with.matches()
        message = called_once_with.explanation.message

        expect(message) == """
A = {0}
B = 2
C = 1
Expected A to be called once with B
Actually called 2 times with C
""".format(mock)

    def test_failure_message_with_wrong_params(self):
        mock = Mock()

        mock(4, 5, 6, c=7)
        called_once_with = CalledOnceWith(mock, 1, False, 2, 3, a=4)
        called_once_with.matches()
        message = called_once_with.explanation.message

        expect(message) == """
A = {0}
B = 1, 2, 3, a=4
C = 4, 5, 6, c=7
Expected A to be called once with B
Actually called 1 times with C
""".format(mock)

    def test_negative_failure_message(self):
        mock = Mock()

        mock(1, 2, 3, a=4)
        called_once_with = CalledOnceWith(mock, 1, True, 2, 3, a=4)
        called_once_with.matches()
        message = called_once_with.explanation.message

        expect(message) == """
A = {0}
B = 1, 2, 3, a=4
C = 1, 2, 3, a=4
Expected A not to be called once with B
Actually called 1 times with C
""".format(mock)

    def test_register(self):
        expect(expect.matcher('called_once_with')) == CalledOnceWith

    def test_not_a_mock(self):
        self.assertRaises(TypeError, CalledOnceWith("a", "b").matches)
        self.assertRaises(TypeError, CalledOnceWith(1, "b").matches)
