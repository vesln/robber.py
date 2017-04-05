from robber import expect
from robber.matchers.boolean import TrueMatcher


class TestTrueMatcher:
    def test_matches(self):
        expect(TrueMatcher(True).matches()).to.eq(True)
        expect(TrueMatcher(False).matches()).to.eq(False)

    def test_failure_message(self):
        true = TrueMatcher(False)
        message = true.failure_message()
        expect(message) == 'Expected False to be True'

    def test_negative_failure_message(self):
        true = TrueMatcher(True, is_negative=True)
        message = true.failure_message()
        expect(message) == 'Expected True to be False'

    def test_register(self):
        expect(expect.matcher('true')) == TrueMatcher
        expect(expect.matcher('false')) == TrueMatcher
