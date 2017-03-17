from unittest import TestCase

from robber import expect
from tests import must_fail


class TestExceptionIntegrations(TestCase):
    def test_exception_success(self):
        expect(lambda: 1 / 0).to.throw(ZeroDivisionError)

    @must_fail
    def test_exception_failure(self):
        expect(lambda: None).to.throw(Exception)
