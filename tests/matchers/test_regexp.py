from robber import expect
from robber.matchers.regexp import Match


class TestMatch:
    def test_matches(self):
        expect(Match('1', r'1').matches()).to.eq(True)
        expect(Match('2', r'1').matches()).to.eq(False)

    def test_explanation_message(self):
        match = Match('actual', r'expected$')
        message = match.explanation.message
        expect(message) == """
A = actual
B = expected$
Expected A to match B
"""

    def test_negative_explanation_message(self):
        match = Match('actual', r'actual$', is_negative=True)
        message = match.explanation.message
        expect(message) == """
A = actual
B = actual$
Expected A not to match B
"""

    def test_register(self):
        expect(expect.matcher('match')) == Match
