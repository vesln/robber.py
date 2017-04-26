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
        message = called_with.explanation.message

        expect(message) == """
A = {0}
B = 2
Expected A to be called with B
Actually not called
""".format(mock)

    def test_failure_message_with_one_arg(self):
        mock = Mock()
        mock(1)

        called_with = CalledWith(mock, 2)
        message = called_with.explanation.message

        expect(message) == """
A = {0}
B = 2
C = 1
Expected A to be called with B
Actually called with C
""".format(mock)

    def test_negative_failure_message_with_one_arg(self):
        mock = Mock()
        mock(2)

        called_with = CalledWith(mock, 2, is_negative=True)
        message = called_with.explanation.message

        expect(message) == """
A = {0}
B = 2
C = 2
Expected A not to be called with B
Actually called with C
""".format(mock)

    def test_failure_message_with_multiple_args(self):
        mock = Mock()

        mock(4, 5, 6, c=7)
        called_with = CalledWith(mock, 1, False, 2, 3, a=4)
        message = called_with.explanation.message

        expect(message) == """
A = {0}
B = 1, 2, 3, a=4
C = 4, 5, 6, c=7
Expected A to be called with B
Actually called with C
""".format(mock)

    def test_negative_failure_message_with_multiple_args(self):
        mock = Mock()

        mock(1, 2, 3, a=4)
        called_with = CalledWith(mock, 1, True, 2, 3, a=4)
        message = called_with.explanation.message

        expect(message) == """
A = {0}
B = 1, 2, 3, a=4
C = 1, 2, 3, a=4
Expected A not to be called with B
Actually called with C
""".format(mock)

    def test_register(self):
        expect(expect.matcher('called_with')) == CalledWith

    def test_not_a_mock(self):
        self.assertRaises(TypeError, CalledWith("a", "b").matches)
        self.assertRaises(TypeError, CalledWith(1, "b").matches)
