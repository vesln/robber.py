from unittest import TestCase

from mock import Mock

from robber import expect
from robber.matchers.ever_called_with import EverCalledWith


class TestEverCalledWith(TestCase):
    def test_matches(self):
        mock = Mock()
        mock(1, 2, 3, a=4)
        mock('other')

        expect(EverCalledWith(mock, 1, False, 2, 3, a=4).matches()).to.eq(True)

    def test_explanation_message(self):
        mock = Mock()
        mock(1, 2, 3, a=4)
        mock('other')

        ever_called_with = EverCalledWith(mock, 5, False, 6, 7, b=8)
        message = ever_called_with.explanation.message

        expect(message) == """
A = {0}
B = 5, 6, 7, b=8
Expected A to have been ever called with B
""".format(mock)

    def test_negative_explanation_message(self):
        mock = Mock()

        mock(1, 2, 3, a=4)
        ever_called_with = EverCalledWith(mock, 1, True, 2, 3, a=4)
        ever_called_with.matches()
        message = ever_called_with.explanation.message

        expect(message) == """
A = {0}
B = 1, 2, 3, a=4
Expected A not to have been ever called with B
""".format(mock)

    def test_register(self):
        expect(expect.matcher('ever_called_with')) == EverCalledWith

    def test_not_a_mock(self):
        self.assertRaises(TypeError, EverCalledWith("a", "b").matches)
        self.assertRaises(TypeError, EverCalledWith(1, "b").matches)
