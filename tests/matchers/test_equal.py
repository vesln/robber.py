from robber import expect
from robber.matchers.equal import Equal


class TestEqual:
    def test_matches(self):
        expect(Equal(1, 1).matches()).to.eq(True)
        expect(Equal(1, 2).matches()).to.eq(False)

    def test_failure_message(self):
        equal = Equal('123', 123)

        expect(equal.explanation.message).to.eq("""
A = '123'
B = 123
Expected A to equal B
""")

    def test_negative_failure_message(self):
        equal = Equal('actual', 'actual', is_negative=True)

        expect(equal.explanation.message).to.eq("""
A = 'actual'
B = 'actual'
Expected A not to equal B
""")

    def test_register(self):
        expect(expect.matcher('eq')) == Equal
        expect(expect.matcher('__eq__')) == Equal
        expect(expect.matcher('ne')) == Equal
        expect(expect.matcher('__ne__')) == Equal
