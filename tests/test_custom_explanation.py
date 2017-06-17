from unittest import TestCase

from termcolor import colored

from robber import expect, BadExpectation, CustomExplanation


class TestCustomExplanation(TestCase):
    def test_custom_error_message(self):
        try:
            with CustomExplanation('Something went wrong'):
                expect(1).to.eq(2)
        except BadExpectation as e:
            expect(e.message) == 'Something went wrong'
        else:
            raise BadExpectation('must fail with custom message')
