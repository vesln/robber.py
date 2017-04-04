from robber import expect
from robber.matchers.base import Base


class Contain(Base):
    """
    expect({'key': value}).to.contain('key')
    expect([1, 2, 3]).to.contain(2)
    """

    def matches(self):
        return self.expected in self.actual

    def failure_message(self):
        return 'Expected {actual}{negative_message} to contain {expected}'.format(
            actual=self.actual, negative_message=self.negative_message, expected=self.expected
        )


class Exclude(Base):
    """
    expect({'key': value}).to.exclude('other')
    expect([1, 2, 3]).to.exclude(4)
    """

    def matches(self):
        return self.expected not in self.actual

    def failure_message(self):
        return 'Expected {actual}{negative_message} to exclude {expected}'.format(
            actual=self.actual, negative_message=self.negative_message, expected=self.expected
        )


expect.register('contain', Contain)
expect.register('exclude', Exclude)
