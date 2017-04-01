from unittest import TestCase

from robber import expect
from robber.matchers.callable import Callable


class TestCallable(TestCase):
    def test_matches(self):
        def a():
            pass

        expect(Callable(a).matches()).to.eq(True)

    def test_failure_message(self):
        assert_callable = Callable("a")
        message = assert_callable.failure_message()
        expect(message) == 'Expected a to be callable'

    def test_failure_message_with_not_to(self):
        def a():
            pass

        assert_callable = Callable(a, is_negated=True)
        message = assert_callable.failure_message()
        expect(message) == 'Expected {a} not to be callable'.format(a=a)

    def test_register(self):
        expect(expect.matcher('callable')) == Callable
