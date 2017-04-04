import re

from robber import expect
from robber.matchers.base import Base


class Match(Base):
    """
    expect('foo').to.match(r'foo')
    """

    def matches(self):
        return bool(re.match(self.expected, self.actual))

    def failure_message(self):
        return 'Expected "{actual}"{negative_message} to match "{expected}"'.format(
            actual=self.actual, negative_message=self.negative_message, expected=self.expected
        )


expect.register('match', Match)
