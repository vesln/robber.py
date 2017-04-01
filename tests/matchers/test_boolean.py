from robber import expect
from robber.matchers.boolean import TrueMatcher, FalseMatcher


class TestTrueMatcher:
    def test_matches(self):
        expect(TrueMatcher(True).matches()).to.eq(True)
        expect(TrueMatcher(False).matches()).to.eq(False)

    def test_failure_message(self):
        true = TrueMatcher(False)
        message = true.failure_message()
        expect(message) == 'Expected False to be True'

    def test_failure_message_with_not_to(self):
        true = TrueMatcher(True, is_negated=True)
        message = true.failure_message()
        expect(message) == 'Expected True not to be True'

    def test_failure_message_with_not_to(self):
        true = TrueMatcher(True, is_negated=True)
        message = true.failure_message()
        expect(message) == 'Expected True not to be True'

    def test_register(self):
        expect(expect.matcher('true')) == TrueMatcher


class TestFalseMatcher:
    def test_matches(self):
        expect(FalseMatcher(False).matches()).to.eq(True)
        expect(FalseMatcher(True).matches()).to.eq(False)

    def test_failure_message(self):
        false = FalseMatcher(True)
        message = false.failure_message()
        expect(message) == 'Expected True to be False'

    def test_failure_message_with_not_to(self):
        false = FalseMatcher(False, is_negated=True)
        message = false.failure_message()
        expect(message) == 'Expected False not to be False'

    def test_register(self):
        expect(expect.matcher('false')) == FalseMatcher
