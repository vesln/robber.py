from robber import expect
from robber.matchers.base import Base


class TestMatcher:
    def __init__(self, actual, expected, is_negative=False):
        expect(actual) == 'test'
        expect(expected) == 'bar'

    def match(self):
        return True

    def fail_with(self, message):
        return self


class TestWillMatch(Base):
    called = False
    message = None

    def matches(self):
        self.called = True
        return True


class TestWontMatch(Base):
    message = None

    def matches(self):
        return False

    def failure_message(self):
        return 'Failure message'


class First:
    pass


class Second:
    pass
