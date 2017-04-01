from unittest import TestCase

from robber import expect
from tests import must_fail


class TestTrueMatcherIntegrations(TestCase):
    def test_true_success(self):
        expect(True).to.be.true()

    @must_fail
    def test_true_failure(self):
        expect(False).to.be.true()

    def test_not_true_success(self):
        expect(False).not_to.be.true()

    @must_fail
    def test_not_true_failure(self):
        expect(True).not_to.be.true()


class TestFalseMatcherIntegrations(TestCase):
    def test_false_success(self):
        expect(False).to.be.false()

    @must_fail
    def test_false_failure(self):
        expect(True).to.be.false()

    def test_not_false_success(self):
        expect(True).not_to.be.false()

    @must_fail
    def test_not_false_success(self):
        expect(False).not_to.be.false()
