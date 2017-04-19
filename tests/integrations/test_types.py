from unittest import TestCase

from robber import expect
from tests import must_fail


class TestStringIntegrations(TestCase):
    # string
    def test_string_success(self):
        expect('test').to.be.a.string()

    @must_fail
    def test_string_failure(self):
        expect(1).to.be.a.string()

    def test_not_to_be_a_string_success(self):
        expect(1).not_to.be.a.string()

    @must_fail
    def test_not_to_be_a_string_failure(self):
        expect('test').not_to.be.a.string()


class TestIntegerIntegrations(TestCase):
    def test_integer_success(self):
        expect(1).to.be.an.integer()

    @must_fail
    def test_integer_failure(self):
        expect('1').to.be.an.integer()

    def test_not_to_be_an_integer_success(self):
        expect('a').not_to.be.an.integer()

    @must_fail
    def test_not_to_be_an_integer_failure(self):
        expect(1).not_to.be.an.integer()


class TestFloatIntegrations(TestCase):
    def test_float_success(self):
        expect(1.0).to.be.a.float()

    @must_fail
    def test_float_failure(self):
        expect(1).to.be.a.float()

    def test_not_to_be_a_float_success(self):
        expect(1).not_to.be.a.float()

    @must_fail
    def test_not_to_be_a_float_failure(self):
        expect(1.0).not_to.be.a.float()


class TestListIntegrations(TestCase):
    def test_list_success(self):
        expect([1, 2]).to.be.a.list()

    @must_fail
    def test_list_failure(self):
        expect('str').to.be.a.list()

    def test_not_to_be_a_list_success(self):
        expect(1).not_to.be.a.list()

    @must_fail
    def test_not_to_be_a_list_failure(self):
        expect([1, 2]).not_to.be.a.list()


class TestDictIntegrations(TestCase):
    def test_dict_success(self):
        expect({}).to.be.a.dict()

    @must_fail
    def test_dict_failure(self):
        expect([]).to.be.a.dict()

    def test_not_to_be_a_dict_success(self):
        expect(1).not_to.be.a.dict()

    @must_fail
    def test_not_to_be_a_dict_failure(self):
        expect({}).not_to.be.a.dict()


class TestTupleIntegrations(TestCase):
    def test_tuple_success(self):
        expect(()).to.be.a.tuple()

    @must_fail
    def test_tuple_failure(self):
        expect([]).to.be.a.tuple()

    def test_not_to_be_a_tuple_success(self):
        expect(1).not_to.be.a.tuple()

    @must_fail
    def test_not_to_be_a_tuple_failure(self):
        expect((1, 2)).not_to.be.a.tuple()


class TestNoneIntegrations(TestCase):
    def test_none_success(self):
        expect(None).to.be.none()

    @must_fail
    def test_none_failure(self):
        expect('str').to.be.none()

    def test_not_to_be_none_success(self):
        expect(1).not_to.be.none()

    @must_fail
    def test_not_to_be_none_failure(self):
        expect(None).not_to.be.none()
