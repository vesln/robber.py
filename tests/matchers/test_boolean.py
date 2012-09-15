import unittest
from robber import expect
from robber.matchers.boolean import TrueMatcher, FalseMatcher

class TestTrueMatcher:
    def test_has_failure_message(self):
        true = TrueMatcher(False)
        message = true.failure_message()
        expect(message) == 'Expected False to be True'

    def test_matches(self):
        expect(TrueMatcher(True).matches()) == True
        expect(TrueMatcher(False).matches()) == False

    def test_it_registers_itself(self):
        expect(expect.matcher('true')) == TrueMatcher

class TestFalseMatcher:
    def test_has_failure_message(self):
        false = FalseMatcher(True)
        message = false.failure_message()
        expect(message) == 'Expected True to be False'

    def test_matches(self):
        expect(FalseMatcher(False).matches()) == True
        expect(FalseMatcher(True).matches()) == False

    def test_it_registers_itself(self):
        expect(expect.matcher('false')) == FalseMatcher
