from unittest import TestCase

from mock import Mock

from robber import expect
from robber.matchers.called import Called


class TestCalled(TestCase):
    def test_matches(self):
        mock = Mock()
        mock()
        expect(Called(mock).matches()).to.eq(True)

    def test_explanation_message(self):
        mock = Mock()
        called = Called(mock)
        message = called.explanation.message
        expect(message) == """
A = {mock}
Expected A to be called
""".format(mock=mock)

    def test_negative_explanation_message(self):
        mock = Mock()
        called = Called(mock, is_negative=True)
        message = called.explanation.message

        mock()

        expect(message) == """
A = {mock}
Expected A not to be called
""".format(mock=mock)

    def test_register(self):
        expect(expect.matcher('called')) == Called

    def test_not_a_mock(self):
        self.assertRaises(TypeError, Called("a").matches)
        self.assertRaises(TypeError, Called(1).matches)
