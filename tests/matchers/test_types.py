import unittest
from robber import expect
from robber.matchers.types import String, Integer, Float, List, Dict, Tuple, Non


class TestString(unittest.TestCase):
    def test_matches(self):
        expect(String('str').matches()).to.eq(True)
        expect(String(1).matches()).to.eq(False)

    def test_failure_message(self):
        string = String(1)
        message = string.explanation.message
        expect(message) == """
A = 1
Expected A to be a string
"""

    def test_negative_failure_message(self):
        string = String('a', is_negative=True)
        message = string.explanation.message
        expect(message) == """
A = 'a'
Expected A not to be a string
"""

    def test_register(self):
        expect(expect.matcher('string')) == String


class TestInteger(unittest.TestCase):
    def test_matches(self):
        expect(Integer(1).matches()).to.eq(True)
        expect(Integer('str').matches()).to.eq(False)

    def test_failure_message(self):
        integer = Integer('a')
        message = integer.explanation.message
        expect(message) == """
A = 'a'
Expected A to be an integer
"""

    def test_negative_failure_message(self):
        integer = Integer(1, is_negative=True)
        message = integer.explanation.message
        expect(message) == """
A = 1
Expected A not to be an integer
"""

    def test_register(self):
        expect(expect.matcher('integer')) == Integer


class TestFloat(unittest.TestCase):
    def test_matches(self):
        expect(Float(1.0).matches()).to.eq(True)
        expect(Float(1).matches()).to.eq(False)

    def test_failure_message(self):
        float_assertion = Float(1)
        message = float_assertion.explanation.message
        expect(message) == """
A = 1
Expected A to be a floating point number
"""

    def test_negative_failure_message(self):
        float_assertion = Float(1.1, is_negative=True)
        message = float_assertion.explanation.message
        expect(message) == """
A = {0}
Expected A not to be a floating point number
""".format(repr(1.1))

    def test_register(self):
        expect(expect.matcher('float')) == Float


class TestArray(unittest.TestCase):
    def test_matches(self):
        expect(List([]).matches()).to.eq(True)
        expect(List(1).matches()).to.eq(False)

    def test_failure_message(self):
        array = List(1)
        message = array.explanation.message
        expect(message) == """
A = 1
Expected A to be an array
"""

    def test_negative_failure_message(self):
        array = List([], is_negative=True)
        message = array.explanation.message
        expect(message) == """
A = []
Expected A not to be an array
"""

    def test_register(self):
        expect(expect.matcher('list')) == List


class TestDict(unittest.TestCase):
    def test_matches(self):
        expect(Dict({}).matches()).to.eq(True)
        expect(Dict(1).matches()).to.eq(False)

    def test_failure_message(self):
        dict_assertion = Dict(1)
        message = dict_assertion.explanation.message
        expect(message) == """
A = 1
Expected A to be a dictionary
"""

    def test_negative_failure_message(self):
        dict_assertion = Dict({}, is_negative=True)
        message = dict_assertion.explanation.message
        expect(message) == """
A = {}
Expected A not to be a dictionary
"""

    def test_register(self):
        expect(expect.matcher('dict')) == Dict


class TestTuple(unittest.TestCase):
    def test_matches(self):
        expect(Tuple((1, 2)).matches()).to.eq(True)
        expect(Tuple(1).matches()).to.eq(False)

    def test_failure_message(self):
        tuple_assertion = Tuple(1)
        message = tuple_assertion.explanation.message
        expect(message) == """
A = 1
Expected A to be a tuple
"""

    def test_negative_failure_message(self):
        tuple_assertion = Tuple((1, 2), is_negative=True)
        message = tuple_assertion.explanation.message
        expect(message) == """
A = (1, 2)
Expected A not to be a tuple
"""

    def test_register(self):
        expect(expect.matcher('tuple')) == Tuple


class TestNone(unittest.TestCase):
    def test_matches(self):
        expect(Non(None).matches()).to.eq(True)
        expect(Non(1).matches()).to.eq(False)

    def test_failure_message(self):
        none = Non(1)
        message = none.explanation.message
        expect(message) == """
A = 1
Expected A to be None
"""

    def test_negative_failure_message(self):
        none = Non(None, is_negative=True)
        message = none.explanation.message
        expect(message) == """
A = None
Expected A not to be None
"""

    def test_register(self):
        expect(expect.matcher('none')) == Non
