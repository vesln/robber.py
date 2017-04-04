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
        return 'Expected "{actual}"{negated_message} to match "{expected}"'.format(
            actual=self.actual, negated_message=self.negated_message, expected=self.expected
        )


expect.register('match', Match)
