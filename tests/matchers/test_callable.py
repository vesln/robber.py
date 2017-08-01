from unittest import TestCase

from robber import expect
from robber.matchers.callable import Callable


class TestCallable(TestCase):
    def test_matches(self):
        def a():
            pass

        expect(Callable(a).matches()).to.eq(True)

    def test_explanation_message(self):
        assert_callable = Callable('string')
        message = assert_callable.explanation.message
        expect(message) == """
A = 'string'
Expected A to be callable
"""

    def test_negative_explanation_message(self):
        def a():
            pass

        assert_callable = Callable(a, is_negative=True)
        message = assert_callable.explanation.message
        expect(message) == """
A = {a}
Expected A not to be callable
""".format(a=a)

    def test_register(self):
        expect(expect.matcher('callable')) == Callable
