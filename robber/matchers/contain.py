from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class Contain(Base):
    """
    expect({'key': value}).to.contain('key 1', 'key 2', 'key n')
    expect([1, 2, 3]).to.contain(1, 2, 3)
    """

    def matches(self):
        expected_list = list(self.args)
        expected_list.insert(0, self.expected)

        if not self.is_negative:
            excluded_args = set(expected_list).difference(self.actual)
            try:
                self.expected_arg = excluded_args.pop()
            except KeyError:
                return True
            else:
                return False

        else:
            # As this is the negative case, we have to flip the return value.
            included_args = set(expected_list).intersection(self.actual)
            try:
                self.expected_arg = included_args.pop()
            except KeyError:
                return False
            else:
                return True

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'contain', self.expected_arg, negative_action='exclude')


expect.register('contain', Contain)
expect.register('exclude', Contain, is_negative=True)
