from robber import expect
from robber.matchers.equal import Equal


class TestEqual:
    def test_matches(self):
        expect(Equal(1, 1).matches()).to.eq(True)
        expect(Equal(1, 2).matches()).to.eq(False)

    def test_failure_message(self):
        equal = Equal('123', 123)
        message = equal.failure_message()
        expect(message) == 'Expected str("123") to equal int("123")'

    def test_negative_failure_message(self):
        equal = Equal('actual', 'actual', is_negative=True)
        message = equal.failure_message()
        expect(message) == 'Expected str("actual") not to equal str("actual")'

    def test_register(self):
        expect(expect.matcher('eq')) == Equal
        expect(expect.matcher('__eq__')) == Equal
        expect(expect.matcher('ne')) == Equal
        expect(expect.matcher('__ne__')) == Equal
