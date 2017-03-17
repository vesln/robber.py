from unittest import TestCase

from robber import expect
from tests import must_fail


class TestTypeIntegrations(TestCase):
    def test_string_success(self):
        expect('test').to.be.a.string()

    @must_fail
    def test_string_failure(self):
        expect(1).to.be.a.string()

    def test_integer_success(self):
        expect(1).to.be.an.integer()

    @must_fail
    def test_integer_failure(self):
        expect('1').to.be.an.integer()

    def test_float_success(self):
        expect(1.0).to.be.a.float()

    @must_fail
    def test_float_failure(self):
        expect(1).to.be.a.float()

    def test_list_success(self):
        expect([1, 2]).to.be.a.list()

    @must_fail
    def test_list_failure(self):
        expect('str').to.be.a.list()

    def test_dict_success(self):
        expect({}).to.be.a.dict()

    @must_fail
    def test_dict_failure(self):
        expect([]).to.be.a.dict()

    def test_tuple_success(self):
        expect(()).to.be.a.tuple()

    @must_fail
    def test_tuple_failure(self):
        expect([]).to.be.a.tuple()

    def test_none_success(self):
        expect(None).to.be.none()

    @must_fail
    def test_none_failure(self):
        expect('str').to.be.none()
