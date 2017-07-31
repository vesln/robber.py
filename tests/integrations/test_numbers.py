from unittest import TestCase

from robber.bad_expectation import BadExpectation

from robber import expect
from tests import must_fail


class TestAboveIntegrations(TestCase):
    def test_above_success(self):
        expect(2).to.be.above(1)

    @must_fail
    def test_above_failure(self):
        expect(1).to.be.above(2)

    def test_not_above_success(self):
        expect(1).not_to.be.above(2)

    @must_fail
    def test_not_above_failure(self):
        expect(2).not_to.be.above(1)


class TestBelowIntegrations(TestCase):
    def test_below_success(self):
        expect(1).to.be.below(2)

    @must_fail
    def test_below_failure(self):
        expect(2).to.be.below(1)

    def test_not_below_success(self):
        expect(2).not_to.be.below(1)

    @must_fail
    def test_not_below_failure(self):
        expect(1).not_to.be.below(2)


class TestWithinIntegrations(TestCase):
    def test_within_success(self):
        expect(2).to.be.within(0, 2)

    @must_fail
    def test_within_failure(self):
        expect(2).to.be.within(3, 4)

    def test_not_within_success(self):
        expect(2).not_to.be.within(3, 4)

    @must_fail
    def test_not_within_failure(self):
        expect(2).not_to.be.within(0, 2)


class TestChangeIntegrations(TestCase):
    @must_fail
    def test_change_by_success(self):
        expect(lambda x: x + 1).to.change(0).by(1)

    # New must_fail does not work with custom chains like this, we have to wrap it manually
    def test_change_by_failure(self):
        try:
            expect(lambda x: x + 1).to.change(0).by(2)
        except BadExpectation:
            pass
        else:
            raise BadExpectation('it must fail')

    def test_not_change_by_success(self):
        expect(lambda x: x + 1).not_to.change(0).by(2)

    def test_not_change_by_failure(self):
        try:
            expect(lambda x: x + 1).not_to.change(0).by(1)
        except BadExpectation:
            pass
        else:
            raise BadExpectation('it must fail')
