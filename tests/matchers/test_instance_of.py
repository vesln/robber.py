from robber import expect
from robber.matchers.instanceof import InstanceOf
from tests.fixtures import First, Second


class TestInstanceOf:
    def test_matches(self):
        expect(InstanceOf(First(), First).matches()).to.eq(True)
        expect(InstanceOf(First(), Second).matches()).to.eq(False)

    def test_explanation_message(self):
        first = First()
        instanceof = InstanceOf(first, First)
        message = instanceof.explanation.message
        expect(message) == """
A = {actual}
B = {expected}
Expected A to be an instance of B
""".format(actual=first, expected=repr(First))

    def test_negative_explanation_message(self):
        first = First()
        instanceof = InstanceOf(first, First, is_negative=True)
        message = instanceof.explanation.message
        expect(message) == """
A = {actual}
B = {expected}
Expected A not to be an instance of B
""".format(actual=first, expected=repr(First))

    def test_register(self):
        expect(expect.matcher('instanceof')) == InstanceOf
