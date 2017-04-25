import unittest
from robber import expect
from robber.matchers.respond_to import RespondTo


class TestRespondTo(unittest.TestCase):
    def test_matches(self):
        expect(RespondTo(expect, 'register').matches()).to.eq(True)
        expect(RespondTo(expect, 'invalid_method').matches()).to.eq(False)

    def test_failure_message(self):
        respond = RespondTo('object', 'method')
        message = respond.explanation.message
        expect(message) == """
A = object
B = method
Expected A to respond to B
"""

    def test_negative_failure_message(self):
        class Foo:
            def bar(self):
                pass

        respond = RespondTo(Foo, 'bar', is_negative=True)
        message = respond.explanation.message
        expect(message) == """
A = {0}
B = 'bar'
Expected A not to respond to B
""".format(Foo)

    def test_register(self):
        expect(expect.matcher('respond_to')) == RespondTo
