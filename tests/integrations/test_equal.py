# -*- coding: utf-8 -*-

from unittest import TestCase

from robber import expect
from tests import must_fail


class TestEqualIntegrations(TestCase):
    def test_eq_success(self):
        expect(1).to.eq(1)
        expect([1, 2]).to.eq([1, 2])
        expect((1, 2)).to.eq((1, 2))
        expect(1).to == 1
        expect(1) == 1
        expect(u'Mèo').to.eq('Mèo')
        expect([u'Mèo', u'Chó']).to.eq(['Mèo', 'Chó'])
        expect([[u'Mèo'], [u'Chó']]).to.eq([['Mèo'], ['Chó']])

    @must_fail
    def test_eq_failure(self):
        expect(1).to.eq(2)
        expect(1).not_to.eq(1)

    def test_ne_success(self):
        expect(1).to.ne(2)
        expect(1).to != 2
        expect(1) != 2

    @must_fail
    def test_ne_failure(self):
        expect(1).to.ne(1)

    def test_not_to_eq_success(self):
        expect(1).not_to.eq(2)
        expect([1, 2]).not_to.eq([2, 1])
        expect((1, 2)).not_to.eq((2, 1))
        expect(1).not_to == 2
