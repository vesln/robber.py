from unittest import TestCase

from mock import Mock

from robber import expect
from tests import must_fail


class TestCalledWithIntegrations(TestCase):
    def test_called_with_one_arg_success(self):
        mock = Mock()
        mock(1)
        expect(mock).to.be.called_with(1)

    def test_called_with_multiple_args_success(self):
        mock = Mock()
        mock(1, 2, 3, a=4, b=5)
        expect(mock).to.be.called_with(1, 2, 3, a=4, b=5)

    @must_fail
    def test_called_with_one_arg_failure(self):
        mock = Mock()
        mock(2)
        expect(mock).to.be.called_with(1)

    @must_fail
    def test_called_with_multiple_args_failure(self):
        mock = Mock()
        mock(1, 2, 3)
        expect(mock).to.be.called_with(1, 2, 3, a=4, b=5)

    def test_called_not_a_mock(self):
        self.assertRaises(TypeError, expect('a').to.be.called)
        self.assertRaises(TypeError, expect(1).to.be.called)

    def test_not_called_with_one_arg_success(self):
        mock = Mock()
        mock(2)
        expect(mock).not_to.be.called_with(1)

    def test_not_called_with_multiple_args_success(self):
        mock = Mock()
        mock(1, 2, 3)
        expect(mock).not_to.be.called_with(1, 2, 3, a=4, b=5)

    @must_fail
    def test_not_called_with_one_arg_failure(self):
        mock = Mock()
        mock(1)
        expect(mock).not_to.be.called_with(1)

    @must_fail
    def test_not_called_with_multiple_args_failure(self):
        mock = Mock()
        mock(1, 2, 3, a=4, b=5)
        expect(mock).not_to.be.called_with(1, 2, 3, a=4, b=5)
