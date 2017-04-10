from robber import expect
from robber.matchers.boolean import Boolean


class TestBooleanMatcher:
    def test_matches(self):
        expect(Boolean(True).matches()).to.eq(True)
        expect(Boolean(False).matches()).to.eq(False)

    def test_failure_message(self):
        true = Boolean(False)
        message = true.failure_message()
        expect(message) == 'Expected False to be True'

    def test_negative_failure_message(self):
        true = Boolean(True, is_negative=True)
        message = true.failure_message()
        expect(message) == 'Expected True to be False'

    def test_register(self):
        expect(expect.matcher('true')) == Boolean
        expect(expect.matcher('false')) == Boolean
