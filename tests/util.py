from robber import BadExpectation
from robber.matchers.base import Base

expectation_count = 0
fail_count = 0

old_match = Base.match


def new_match(self):
    global expectation_count
    expectation_count += 1

    try:
        old_match(self)
    except BadExpectation:
        global fail_count
        fail_count += 1


def reset():
    global expectation_count
    global fail_count

    Base.match = old_match
    expectation_count = 0
    fail_count = 0


def must_fail(fn):
    """
    This checks if every expectation in a test fails.
    """

    def test_decorated(self, *args, **kwargs):
        Base.match = new_match
        fn(self, *args, **kwargs)
        message = 'The test has {expectation_count} expectations, only {fail_count} fails.'.format(
            expectation_count=expectation_count, fail_count=fail_count
        )

        if fail_count < expectation_count:
            reset()
            raise BadExpectation(message)

        reset()

    test_decorated.__name__ = fn.__name__

    return test_decorated
