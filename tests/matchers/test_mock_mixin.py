from unittest import TestCase

from mock import Mock, call

from robber.expect import expect
from robber.matchers.base import Base
from robber.matchers.mock_mixin import MockMixin


class DummyMockMatcher(Base, MockMixin):
    pass


class TestCallArgs(TestCase):
    def test_with_args_and_kwargs(self):
        dummy_matcher = DummyMockMatcher(Mock(), 1, False, a='a', one=1)
        expect(dummy_matcher.call_args).to.eq(call(1, a='a', one=1))

    def test_with_kwargs(self):
        dummy_matcher = DummyMockMatcher(Mock(), None, False, a='a', one=1)
        expect(dummy_matcher.call_args).to.eq(call(a='a', one=1))


class TestCallArgsStr(TestCase):
    def test_with_no_params(self):
        actual = Mock()
        dummy_matcher = DummyMockMatcher(actual)

        actual()

        expect(dummy_matcher.call_args_str).to.eq('no arguments')

    def test_with_args_and_kwargs(self):
        actual = Mock()
        dummy_matcher = DummyMockMatcher(actual)

        actual(1, 'a', 3, a=1, b=2)

        expect(dummy_matcher.call_args_str).to.eq("1, 'a', 3, a=1, b=2")


class TestExpectedArgs(TestCase):
    def test_with_no_params(self):
        dummy_matcher = DummyMockMatcher(Mock())
        expect(dummy_matcher.expected_args_str).to.eq('no arguments')

    def test_with_expected(self):
        dummy_matcher = DummyMockMatcher(Mock(), 1)
        expect(dummy_matcher.expected_args_str).to.eq('1')

    def test_with_expected_and_args(self):
        dummy_matcher = DummyMockMatcher(Mock(), 1, False, 2, 'a')
        expect(dummy_matcher.expected_args_str).to.eq("1, 2, 'a'")

    def test_with_only_kwargs(self):
        dummy_matcher = DummyMockMatcher(Mock(), a='a')

        expect(dummy_matcher.expected_args_str).to.eq("a='a'")

    def test_with_expected_and_kwargs(self):
        dummy_matcher = DummyMockMatcher(Mock(), 1, False, a='a', one=1)
        split_expected_args = dummy_matcher.expected_args_str.split(', ')

        # Since we cannot be sure about the order of a dict, which leads to the situation that the function
        # build_expected_params_string can return different results (still acceptable). In order to test, we will split
        # the result into smaller parts, and assert each one.
        expect(split_expected_args).to.contain('1')
        expect(split_expected_args).to.contain("a='a'")
        expect(split_expected_args).to.contain('one=1')

    def test_with_expected_and_args_and_kwargs(self):
        dummy_matcher = DummyMockMatcher(Mock(), 1, False, 2, 'a', b='b', one=1)
        split_expected_args = dummy_matcher.expected_args_str.split(', ')

        expect(split_expected_args).to.contain('1')
        expect(split_expected_args).to.contain('2')
        expect(split_expected_args).to.contain("'a'")
        expect(split_expected_args).to.contain("b='b'")
        expect(split_expected_args).to.contain('one=1')
