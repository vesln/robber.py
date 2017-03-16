from unittest.case import TestCase

from robber import expect, BadExpectation, failure_message


class TestCustomErrorMessageIntegrations(TestCase):
    def test_custom_error_message(self):
        try:
            with failure_message('Something went wrong'):
                expect(1).to.eq(2)
        except BadExpectation as e:
            expect(e.message) == 'Something went wrong'
        else:
            raise BadExpectation('must fail with custom message')
