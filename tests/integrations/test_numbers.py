from unittest.case import TestCase

from robber import expect
from tests import must_fail


class TestNumbersIntegrations(TestCase):
    def test_above_success(self):
        expect(2).to.be.above(1)

    @must_fail
    def test_above_success(self):
        expect(1).to.be.above(2)

    def test_below_success(self):
        expect(1).to.be.below(2)

    @must_fail
    def test_below_failure(self):
        expect(2).to.be.below(1)

    def test_within_success(self):
        expect(2).to.be.within(0, 2)

    @must_fail
    def test_within_failure(self):
        expect(2).to.be.within(3, 4)

    def test_change_by_success(self):
        expect(lambda x: x + 1).to.change(0).by(1)

    @must_fail
    def test_change_by_failure(self):
        expect(lambda x: x + 1).to.change(0).by(2)
