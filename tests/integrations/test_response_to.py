from unittest.case import TestCase

from robber import expect
from tests import must_fail


class TestResponseTo(TestCase):
    def test_respond_to_success(self):
        expect(expect).to.respond_to('register')

    @must_fail
    def test_respond_to_failure(self):
        expect(expect).to.respond_to('undefined_method')
