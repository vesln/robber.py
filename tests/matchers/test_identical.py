import unittest
from robber import expect, BadExpectation
from robber.matchers.identical import Identical, NotIdentical

class TestIdentical:
    def test_has_failure_message(self):
        identical = Identical('actual', 'expected')
        message = identical.failure_message()
        expect(message) == 'Expected "actual" to be "expected"'

    def test_matches(self):
        expect(Identical(1, 1).matches()) == True
        expect(Identical({0: 1}, {0: 1}).matches()) == False

    def test_it_registers_itself(self):
        expect(expect.matcher('equal')) == Identical

class TestNotIdentical:
    def test_has_failure_message(self):
        identical = NotIdentical('actual', 'expected')
        message = identical.failure_message()
        expect(message) == 'Expected "actual" not to be "expected"'

    def test_matches(self):
        expect(NotIdentical({0: 1}, {0: 1}).matches()) == True
        expect(NotIdentical(1, 1).matches()) == False

    def test_it_registers_itself(self):
        expect(expect.matcher('not_equal')) == NotIdentical
