from robber import expect
from robber.matchers.regexp import Match


class TestMatch:
    def test_matches(self):
        expect(Match('1', r'1').matches()).to.eq(True)
        expect(Match('2', r'1').matches()).to.eq(False)

    def test_failure_message(self):
        match = Match('actual', r'expected$')
        message = match.failure_message()
        expect(message) == 'Expected "actual" to match "expected$"'

    def test_failure_message_with_not_to(self):
        match = Match('actual', r'actual$', is_negative=True)
        message = match.failure_message()
        expect(message) == 'Expected "actual" not to match "actual$"'

    def test_register(self):
        expect(expect.matcher('match')) == Match
