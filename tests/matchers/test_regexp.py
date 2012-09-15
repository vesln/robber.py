import unittest
from robber import expect
from robber.matchers.regexp import Match, NotMatch

class TestMatch:
    def test_has_failure_message(self):
        match = Match('actual', r'expected$')
        message = match.failure_message()
        expect(message) == 'Expected "actual" to match "expected$"'

    def test_matches(self):
        expect(Match('1', r'1').matches()) == True
        expect(Match('2', r'1').matches()) == False

    def test_it_registers_itself(self):
        expect(expect.matcher('match')) == Match

class TestNotMatch:
    def test_has_failure_message(self):
        not_match = NotMatch('actual', r'expected$')
        message = not_match.failure_message()
        expect(message) == 'Expected "actual" to not match "expected$"'

    def test_matches(self):
        expect(NotMatch('2', r'1').matches()) == True
        expect(NotMatch('1', r'1').matches()) == False

    def test_it_registers_itself(self):
        expect(expect.matcher('not_match')) == NotMatch
