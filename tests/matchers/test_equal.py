import unittest
from robber import expect
from robber.matchers.equal import Equal, NotEqual

class TestEqual:
    def test_has_failure_message(self):
        equal = Equal('actual', 'expected')
        message = equal.failure_message()
        expect(message) == 'Expected "actual" to equal "expected"'

    def test_matches(self):
        expect(Equal(1, 1).matches()) == True
        expect(Equal(1, 2).matches()) == False

    def test_it_registers_itself(self):
        expect(expect.matcher('eq')) == Equal
        expect(expect.matcher('__eq__')) == Equal

class TestNotEqual:
    def test_has_failure_message(self):
        equal = NotEqual('actual', 'expected')
        message = equal.failure_message()
        expect(message) == 'Expected "actual" to not equal "expected"'

    def test_matches(self):
        expect(NotEqual(1, 2).matches()) == True
        expect(NotEqual(1, 1).matches()) == False

    def test_it_registers_itself(self):
        expect(expect.matcher('not_eq')) == NotEqual
        expect(expect.matcher('ne')) == NotEqual
        expect(expect.matcher('__ne__')) == NotEqual
