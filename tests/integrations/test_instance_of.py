from unittest import TestCase

from robber import expect
from tests import must_fail


class TestInstanceIntegrations(TestCase):
    def test_instance_of_success(self):
        expect(expect(None)).to.be.instance_of(expect)

    @must_fail
    def test_instance_of_failure(self):
        expect(expect(None)).to.be.instance_of(TestCase)

    def test_not_to_be_instance_of_success(self):
        expect(expect(None)).not_to.be.instance_of(TestCase)

    @must_fail
    def test_not_to_be_instance_of_failure(self):
        expect(expect(None)).not_to.be.instance_of(expect)
