from unittest.case import TestCase

from robber import expect
from tests import must_fail


class TestTruthyIntegrations(TestCase):
    def test_truthy_success(self):
        expect(['test']).to.be.truthy()

    @must_fail
    def test_truthy_failure(self):
        expect([]).to.be.truthy()

    def test_falsy_success(self):
        expect([]).to.be.falsy()

    @must_fail
    def test_falsy_failure(self):
        expect(['test']).to.be.falsy()
