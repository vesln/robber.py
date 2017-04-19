from unittest import TestCase

from robber import expect
from tests import must_fail


class TestLengthIntegrations(TestCase):
    def test_length_success(self):
        expect([1, 2]).to.have.length(2)

    @must_fail
    def test_length_failure(self):
        expect([1, 2]).to.have.length(3)

    def test_length_with_not_to_success(self):
        expect([1, 2]).not_to.have.length(3)

    @must_fail
    def test_length_with_not_to_failure(self):
        expect([1, 2]).not_to.have.length(2)


class TestEmptyIntegrations(TestCase):
    def test_empty_success(self):
        expect('').to.be.empty()

    @must_fail
    def test_empty_failure(self):
        expect('test').to.be.empty()

    def test_not_empty_success(self):
        expect('test').not_to.be.empty()

    @must_fail
    def test_not_empty_failure(self):
        expect('').not_to.be.empty()
