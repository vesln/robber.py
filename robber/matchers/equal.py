from difflib import Differ

from robber import expect
from robber.constants import DIFF_BUILDABLE_TYPES
from robber.explanation import Explanation
from robber.matchers.base import Base


class Equal(Base):
    """
    expect(1).to.eq(1)
    expect(1).to == 1
    expect(1) == 1
    """

    def matches(self):
        return self.actual == self.expected

    @property
    def explanation(self):
        if type(self.actual) is dict and type(self.expected) is dict:
            return Explanation(self.actual, self.is_negative, 'equal', self.expected, more_detail=self.dict_diffs)

        return Explanation(self.actual, self.is_negative, 'equal', self.expected, more_detail=self.diffs)

    @property
    def dict_diffs(self):
        if len(self.actual) != len(self.expected):
            return 'A and B does not have the same length'

        for k in self.actual:
            try:
                val_a = self.actual[k]
                val_b = self.expected[k]
                if not val_a == val_b:
                    return "A['{key}'] = {val_a} while B['{key}'] = {val_b}".format(key=k, val_a=val_a, val_b=val_b)
            except KeyError:
                return "A has key '{k}' while B does not".format(k=k)

    @property
    def diffs(self):
        actual = self.actual
        expected = self.expected

        if actual == expected:
            return ''

        if type(actual) is not type(expected):
            return ''

        object_type = type(actual)

        if object_type not in DIFF_BUILDABLE_TYPES:
            return ''

        if object_type is not str:
            actual = repr(actual)
            expected = repr(expected)

        differ = Differ()
        diffs = differ.compare(actual.splitlines(), expected.splitlines())
        return 'Diffs:\n{0}'.format('\n'.join(diffs))


expect.register('eq', Equal)
expect.register('__eq__', Equal)

expect.register('ne', Equal, is_negative=True)
expect.register('__ne__', Equal, is_negative=True)
