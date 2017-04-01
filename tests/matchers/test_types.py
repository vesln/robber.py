import unittest
from robber import expect
from robber.matchers.types import String, Integer, Float, List, Dict, Tuple, Non


class TestString(unittest.TestCase):
    def test_matches(self):
        expect(String('str').matches()).to.eq(True)
        expect(String(1).matches()).to.eq(False)

    def test_failure_message(self):
        string = String(1)
        expect(string.failure_message()) == 'Expected "1" to be a string'

    def test_failure_message_with_not_to(self):
        string = String('a', is_negative=True)
        expect(string.failure_message()) == 'Expected "a" not to be a string'

    def test_register(self):
        expect(expect.matcher('string')) == String


class TestInteger(unittest.TestCase):
    def test_matches(self):
        expect(Integer(1).matches()).to.eq(True)
        expect(Integer('str').matches()).to.eq(False)

    def test_failure_message(self):
        integer = Integer('a')
        expect(integer.failure_message()) == 'Expected "a" to be an integer'

    def test_failure_message_with_not_to(self):
        integer = Integer(1, is_negative=True)
        expect(integer.failure_message()) == 'Expected "1" not to be an integer'

    def test_register(self):
        expect(expect.matcher('integer')) == Integer


class TestFloat(unittest.TestCase):
    def test_matches(self):
        expect(Float(1.0).matches()).to.eq(True)
        expect(Float(1).matches()).to.eq(False)

    def test_failure_message(self):
        float_assertion = Float(1)
        expect(float_assertion.failure_message()) == 'Expected "1" to be a floating point number'

    def test_failure_message_with_not_to(self):
        float_assertion = Float(1.1, is_negative=True)
        expect(float_assertion.failure_message()) == 'Expected "1.1" not to be a floating point number'

    def test_register(self):
        expect(expect.matcher('float')) == Float


class TestArray(unittest.TestCase):
    def test_matches(self):
        expect(List([]).matches()).to.eq(True)
        expect(List(1).matches()).to.eq(False)

    def test_failure_message(self):
        array = List(1)
        expect(array.failure_message()) == 'Expected "1" to be an array'

    def test_failure_message_not_to(self):
        array = List([], is_negative=True)
        expect(array.failure_message()) == 'Expected "[]" not to be an array'

    def test_register(self):
        expect(expect.matcher('list')) == List


class TestDict(unittest.TestCase):
    def test_matches(self):
        expect(Dict({}).matches()).to.eq(True)
        expect(Dict(1).matches()).to.eq(False)

    def test_failure_message(self):
        dict_assertion = Dict(1)
        expect(dict_assertion.failure_message()) == 'Expected "1" to be a dictionary'

    def test_failure_message_with_not_to(self):
        dict_assertion = Dict({}, is_negative=True)
        expect(dict_assertion.failure_message()) == 'Expected "{}" not to be a dictionary'

    def test_register(self):
        expect(expect.matcher('dict')) == Dict


class TestTuple(unittest.TestCase):
    def test_matches(self):
        expect(Tuple((1, 2)).matches()).to.eq(True)
        expect(Tuple(1).matches()).to.eq(False)

    def test_failure_message(self):
        tuple_assertion = Tuple(1)
        expect(tuple_assertion.failure_message()) == 'Expected "1" to be a tuple'

    def test_failure_message_with_not_to(self):
        tuple_assertion = Tuple((1, 2), is_negative=True)
        expect(tuple_assertion.failure_message()) == 'Expected "(1, 2)" not to be a tuple'

    def test_register(self):
        expect(expect.matcher('tuple')) == Tuple


class TestNone(unittest.TestCase):
    def test_matches(self):
        expect(Non(None).matches()).to.eq(True)
        expect(Non(1).matches()).to.eq(False)

    def test_failure_message(self):
        none = Non(1)
        expect(none.failure_message()) == 'Expected "1" to be None'

    def test_failure_message_with_not_to(self):
        none = Non(None, is_negative=True)
        expect(none.failure_message()) == 'Expected "None" not to be None'

    def test_register(self):
        expect(expect.matcher('none')) == Non
