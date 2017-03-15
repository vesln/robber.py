from unittest import TestCase

from robber import expect
from robber.matchers.callable import Callable


class TestCallable(TestCase):
    def test_matches(self):
        def a():
            pass

        expect(Callable(a).matches()) == True

    def test_failure_message(self):
        callable = Callable("a")
        message = callable.failure_message()
        expect(message) == 'Expected a to be callable'

    def test_register(self):
        expect(expect.matcher('callable')) == Callable
        expect(expect.matcher('__callable__')) == Callable
