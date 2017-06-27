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
            included, self.expected_arg = self._contain(self.actual, expected_list)
            return included

        else:
            excluded, self.expected_arg = self._exclude(self.actual, expected_list)
            # As this is the negative case, we have to flip the return value.
            return not excluded

    @staticmethod
    def _contain(source_list, target_list):
        # checks if source_list includes target_list and returns the first excluded element if yes
        excluded_elements = set(target_list).difference(source_list)
        try:
            first_excluded_element = excluded_elements.pop()
        except KeyError:
            return True, None
        else:
            return False, first_excluded_element

    @staticmethod
    def _exclude(source_list, target_list):
        # checks if source_list excludes target_list and returns the first included element if yes
        included_elements = set(target_list).intersection(source_list)
        try:
            first_included_element = included_elements.pop()
        except KeyError:
            return True, None
        else:
            return False, first_included_element

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'contain', self.expected_arg, negative_action='exclude')


expect.register('contain', Contain)
expect.register('exclude', Contain, is_negative=True)
