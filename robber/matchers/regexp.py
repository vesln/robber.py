import re

from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class Match(Base):
    """
    expect('foo').to.match(r'foo')
    """

    def matches(self):
        return bool(re.match(self.expected, self.actual))

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'match', self.expected)


expect.register('match', Match)
