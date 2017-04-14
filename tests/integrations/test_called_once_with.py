from unittest import TestCase

from mock import Mock

from robber import expect
from tests import must_fail


class TestCalledOnceWithIntegrations(TestCase):
    def test_called_once_with_success(self):
        mock = Mock()
        mock(1, 2, 3, a=4, b=5)
        expect(mock).to.be.called_once_with(1, 2, 3, a=4, b=5)

    @must_fail
    def test_called_once_with_failure(self):
        mock = Mock()
        mock(1, 2, 3)
        expect(mock).to.be.called_once_with(1, 2, 3, a=4, b=5)

    @must_fail
    def test_not_called(self):
        mock = Mock()
        expect(mock).to.be.called_once_with(1)

    @must_fail
    def test_called_once_with_failure_with_called_many_times(self):
        mock = Mock()
        mock(1, 2, 3, a=4, b=5)
        mock(1, 2, 3, a=4, b=5)
        expect(mock).to.be.called_once_with(1, 2, 3, a=4, b=5)

    def test_called_not_a_mock(self):
        self.assertRaises(TypeError, expect('a').to.be.called_once_with)
        self.assertRaises(TypeError, expect(1).to.be.called_once_with)

    def test_not_called_once_with_success(self):
        mock = Mock()
        mock(1, 2, 3)
        expect(mock).not_to.be.called_once_with(1, 2, 3, a=4, b=5)

    @must_fail
    def test_not_called_once_with_failure(self):
        mock = Mock()
        mock(1, 2, 3, a=4, b=5)
        expect(mock).not_to.be.called_once_with(1, 2, 3, a=4, b=5)
