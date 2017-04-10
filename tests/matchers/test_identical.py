from robber import expect
from robber.matchers.identical import Identical


class TestIdentical:
    def test_matches(self):
        expect(Identical(1, 1).matches()).to.eq(True)
        expect(Identical({0: 1}, {0: 1}).matches()).to.eq(False)

    def test_failure_message(self):
        identical = Identical('actual', 'expected')
        message = identical.failure_message()
        expect(message) == 'Expected "actual" to be "expected"'

    def test_negative_failure_message(self):
        identical = Identical('actual', 'actual', is_negative=True)
        message = identical.failure_message()
        expect(message) == 'Expected "actual" not to be "actual"'

    def test_register(self):
        expect(expect.matcher('equal')) == Identical
