from unittest import TestCase

from mock.mock import Mock

from robber import expect
from tests import must_fail


class TestCalledIntegrations(TestCase):
    def test_called_success(self):
        mock = Mock()
        mock()
        expect(mock).to.be.called()

    @must_fail
    def test_called_failure(self):
        mock = Mock()
        expect(mock).to.be.called()

    def test_called_not_a_mock(self):
        self.assertRaises(TypeError, expect('a').to.be.called)
        self.assertRaises(TypeError, expect(1).to.be.called)
