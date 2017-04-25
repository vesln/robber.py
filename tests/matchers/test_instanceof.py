from robber import expect
from robber.matchers.instance_of import InstanceOf
from tests.fixtures import First, Second


class TestInstanceOf:
    def test_matches(self):
        expect(InstanceOf(First(), First).matches()).to.eq(True)
        expect(InstanceOf(First(), Second).matches()).to.eq(False)

    def test_failure_message(self):
        first = First()
        instance_of = InstanceOf(first, First)
        message = instance_of.failure_message()
        expect(message) == 'Expected "{actual}" to be an instance of "{expected}"'.format(
            actual=first, expected=First
        )

    def test_negative_failure_message(self):
        first = First()
        instance_of = InstanceOf(first, First, is_negative=True)
        message = instance_of.failure_message()
        expect(message) == 'Expected "{actual}" not to be an instance of "{expected}"'.format(
            actual=first, expected=First
        )

    def test_register(self):
        expect(expect.matcher('instance_of')) == InstanceOf
