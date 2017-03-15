import unittest

from mock.mock import Mock

from robber import expect, BadExpectation, failure_message
from tests import must_fail


class TestIntegration(unittest.TestCase):
    def test_eq_success(self):
        expect(1).to.eq(1)
        expect([1, 2]).to.eq([1, 2])
        expect((1, 2)).to.eq((1, 2))
        expect(1).to == 1
        expect(1) == 1

    @must_fail
    def test_eq_failure(self):
        expect(1).to.eq(2)

    def test_ne_success(self):
        expect(1).to.ne(2)
        expect(1).to.not_eq(2)
        expect(1).to != 2
        expect(1) != 2

    @must_fail
    def test_ne_failure(self):
        expect(1).to.ne(1)

    def test_equal_success(self):
        expect(1).to.equal(1)
        expect('foo').to.equal('foo')
        dict = {0: 1}
        expect(dict).to.equal(dict)

    @must_fail
    def test_equal_failure(self):
        expect({0: 1}).to.equal({0: 1})

    def test_not_equal_success(self):
        expect(1).to.not_equal(2)

    @must_fail
    def test_equal_failure(self):
        expect(1).to.not_equal(1)

    def test_true_success(self):
        expect(True).to.be.true()

    @must_fail
    def test_true_failure(self):
        expect(False).to.be.true()

    def test_false_success(self):
        expect(False).to.be.false()

    @must_fail
    def test_false_failure(self):
        expect(True).to.be.false()

    def test_instancef(self):
        expect(expect(None)).to.be.instanceof(expect)

    @must_fail
    def test_instancef(self):
        expect(expect(None)).to.be.instanceof(unittest.TestCase)

    def test_match_success(self):
        expect('foo').to.match(r'foo')

    @must_fail
    def test_match_failure(self):
        expect('bar').to.match(r'foo')

    def test_not_match_success(self):
        expect('bar').to.not_match(r'foo')

    @must_fail
    def test_not_match_failure(self):
        expect('foo').to.not_match(r'foo')

    def test_respond_to_success(self):
        expect(expect).to.respond_to('register')

    @must_fail
    def test_respond_to_failure(self):
        expect(expect).to.respond_to('undefined_method')

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

    def test_length_success(self):
        expect([1, 2]).to.have.length(2)

    @must_fail
    def test_length_success(self):
        expect([1, 2]).to.have.length(3)

    def test_empty_success(self):
        expect('').to.be.empty()

    @must_fail
    def test_empty_failure(self):
        expect('test').to.be.empty()

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

    def test_contain_success(self):
        expect([1, 2, 3]).to.contain(2)

    @must_fail
    def test_contain_failure(self):
        expect([1, 2, 3]).to.contain(4)

    def test_custom_error_message(self):
        try:
            with failure_message('Something went wrong'):
                expect(1).to.eq(2)
        except BadExpectation as e:
            expect(e.message) == 'Something went wrong'
        else:
            raise BadExpectation('must fail with custom message')

    def test_change_by_success(self):
        expect(lambda x: x + 1).to.change(0).by(1)

    @must_fail
    def test_change_by_failure(self):
        expect(lambda x: x + 1).to.change(0).by(2)

    def test_exception_success(self):
        expect(lambda: 1 / 0).to.throw(ZeroDivisionError)

    @must_fail
    def test_exception_success(self):
        expect(lambda: None).to.throw(Exception)

    def test_called_success(self):
        mock = Mock()
        mock()
        expect(mock).to.be.called()

    @must_fail
    def test_called_failure(self):
        mock = Mock()
        expect(mock).to.be.called()

    def test_not_a_mock(self):
        self.assertRaises(TypeError, expect('a').to.be.called)
        self.assertRaises(TypeError, expect(1).to.be.called)
