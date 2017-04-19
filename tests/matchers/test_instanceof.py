from robber import expect
from robber.matchers.instanceof import Instanceof
from tests.fixtures import First, Second


class TestInstanceof:
    def test_matches(self):
        expect(Instanceof(First(), First).matches()).to.eq(True)
        expect(Instanceof(First(), Second).matches()).to.eq(False)

    def test_failure_message(self):
        first = First()
        instanceof = Instanceof(first, First)
        message = instanceof.failure_message()
        expect(message) == 'Expected "{actual}" to be an instance of "{expected}"'.format(
            actual=first, expected=First
        )

    def test_negative_failure_message(self):
        first = First()
        instanceof = Instanceof(first, First, is_negative=True)
        message = instanceof.failure_message()
        expect(message) == 'Expected "{actual}" not to be an instance of "{expected}"'.format(
            actual=first, expected=First
        )

    def test_register(self):
        expect(expect.matcher('instanceof')) == Instanceof
