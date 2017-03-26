from robber import expect
from robber.matchers.equal import Equal, NotEqual


class TestEqual:
    def test_matches(self):
        expect(Equal(1, 1).matches()) is True
        expect(Equal(1, 2).matches()) is False

    def test_failure_message(self):
        equal = Equal('actual', 'expected')
        message = equal.failure_message()
        expect(message) == 'Expected "actual" to equal "expected"'

    def test_register(self):
        expect(expect.matcher('eq')) == Equal
        expect(expect.matcher('__eq__')) == Equal


class TestNotEqual:
    def test_matches(self):
        expect(NotEqual(1, 2).matches()) is True
        expect(NotEqual(1, 1).matches()) is False

    def test_failure_message(self):
        equal = NotEqual('actual', 'expected')
        message = equal.failure_message()
        expect(message) == 'Expected "actual" not to equal "expected"'

    def test_register(self):
        expect(expect.matcher('not_eq')) == NotEqual
        expect(expect.matcher('ne')) == NotEqual
        expect(expect.matcher('__ne__')) == NotEqual
