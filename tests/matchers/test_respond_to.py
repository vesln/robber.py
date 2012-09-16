import unittest
from robber import expect
from robber.matchers.respond_to import RespondTo

class TestRespondTo:
    def test_matches(self):
        expect(RespondTo(expect, 'register').matches()) == True
        expect(RespondTo(expect, 'invalid_method').matches()) == False

    def test_failure_message(self):
        respond = RespondTo('object', 'method')
        expect(respond.failure_message()) == 'Expected "object" to respond to "method"'

    def test_register(self):
        expect(expect.matcher('respond_to')) == RespondTo
