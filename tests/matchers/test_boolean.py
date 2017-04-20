from robber import expect
from robber.matchers.boolean import Boolean


class TestBooleanMatcher:
    def test_matches(self):
        expect(Boolean(True).matches()).to.eq(True)
        expect(Boolean(False).matches()).to.eq(False)

    def test_failure_message(self):
        boolean = Boolean(False)
        expect(boolean.explanation.message).to.eq("""
A = False
Expected A to be True
""")

    def test_negative_failure_message(self):
        boolean = Boolean(True, is_negative=True)
        expect(boolean.explanation.message).to.eq("""
A = True
Expected A to be False
""")

    def test_register(self):
        expect(expect.matcher('true')) == Boolean
        expect(expect.matcher('false')) == Boolean
