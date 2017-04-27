from unittest import TestCase

from mock import Mock

from robber import expect
from robber.matchers.called_once import CalledOnce


class TestCalledOnce(TestCase):
    def test_matches(self):
        mock = Mock()
        mock()
        expect(CalledOnce(mock).matches()).to.eq(True)

    def test_explanation_message(self):
        mock = Mock()
        called_once = CalledOnce(mock)
        message = called_once.explanation.message
        expect(message) == """
A = {mock}
Expected A to be called once
Called 0 times
""".format(mock=mock)

    def test_negative_explanation_message(self):
        mock = Mock()
        mock()
        called_once = CalledOnce(mock, is_negative=True)
        message = called_once.explanation.message

        expect(message) == """
A = {mock}
Expected A not to be called once
But it happened
""".format(mock=mock)

    def test_register(self):
        expect(expect.matcher('called_once')) == CalledOnce

    def test_not_a_mock(self):
        self.assertRaises(TypeError, CalledOnce("a").matches)
        self.assertRaises(TypeError, CalledOnce(1).matches)
