from unittest import TestCase

from mock import Mock

from robber import expect
from tests import must_fail


class TestAnyCallIntegrations(TestCase):
    def test_ever_called_with_success(self):
        mock = Mock()
        mock(1, 2, 3, a=4, b=5)
        mock('other')

        expect(mock).to.have.been.ever_called_with(1, 2, 3, a=4, b=5)

    @must_fail
    def test_ever_called_with_failure(self):
        mock = Mock()
        mock(1, 2, 3)
        mock('other')

        expect(mock).to.have.been.ever_called_with(1, 2, 3, a=4, b=5)

    def test_called_not_a_mock(self):
        self.assertRaises(TypeError, expect('a').to.have.been.ever_called_with)
        self.assertRaises(TypeError, expect(1).to.have.been.ever_called_with)

    def test_not_ever_called_with_success(self):
        mock = Mock()
        mock(1, 2, 3)
        mock('other')

        expect(mock).not_to.have.been.ever_called_with(1, 2, 3, a=4, b=5)

    @must_fail
    def test_not_ever_called_with_failure(self):
        mock = Mock()
        mock(1, 2, 3, a=4, b=5)
        mock('other')

        expect(mock).not_to.have.been.ever_called_with(1, 2, 3, a=4, b=5)
