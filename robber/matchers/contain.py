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
            # run when contain chain triggered
            elements = set(expected_list).difference(self.actual)

        else:
            # run when not contain/excluded chain triggered
            elements = set(expected_list).intersection(self.actual)

        existed, self.expected_arg = self._get_first(elements)
        return existed is self.is_negative

    @staticmethod
    def _get_first(elements):
        try:
            first_element = elements.pop()
        except KeyError:
            return False, None
        else:
            return True, first_element

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'contain', self.expected_arg, negative_action='exclude')


expect.register('contain', Contain)
expect.register('exclude', Contain, is_negative=True)
