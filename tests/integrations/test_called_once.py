from unittest import TestCase

from mock import Mock

from robber import expect
from tests import must_fail


class TestCalledOnceIntegrations(TestCase):
    def test_called_once_success(self):
        mock = Mock()
        mock()
        expect(mock).to.be.called_once()

    @must_fail
    def test_called_once_failure_with_not_called(self):
        mock = Mock()
        expect(mock).to.be.called_once()

    @must_fail
    def test_called_once_failure_with_called_many_times(self):
        mock = Mock()
        mock()
        mock()
        expect(mock).to.be.called_once()

    def test_called_once_not_a_mock(self):
        self.assertRaises(TypeError, expect('a').to.be.called_once)
        self.assertRaises(TypeError, expect(1).to.be.called_once)

    def test_not_called_once_success(self):
        mock = Mock()
        expect(mock).not_to.be.called_once()

    @must_fail
    def test_not_called_once_failure(self):
        mock = Mock()
        mock()
        expect(mock).not_to.be.called_once()
