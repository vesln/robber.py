from difflib import Differ

from robber import expect
from robber.explanation import Explanation
from robber.helper import Helper
from robber.matchers.base import Base


class Equal(Base):
    """
    expect(1).to.eq(1)
    expect(1) == 1
    expect(1).to.ne(1)
    expect(1) != 1
    """

    def matches(self):
        self.standardize_args()
        return self.actual == self.expected

    @property
    def explanation(self):
        if type(self.actual) is dict and type(self.expected) is dict:
            more_detail = self.dict_diffs
        elif type(self.actual) is list and type(self.expected) is list:
            more_detail = self.list_diffs
        elif type(self.actual) is str and type(self.expected) is str:
            more_detail = self.str_diffs
        else:
            more_detail = None

        return Explanation(self.actual, self.is_negative, 'equal', self.expected, more_detail=more_detail)

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
    def list_diffs(self):
        if len(self.actual) != len(self.expected):
            return 'A and B does not have the same length'

        for m in self.actual:
            if m not in self.expected:
                return "A contains {m} while B does not".format(m=m)

    @property
    def str_diffs(self):
        if self.actual == self.expected:
            return ''

        differ = Differ()
        diffs = differ.compare(self.actual.splitlines(), self.expected.splitlines())
        return 'Diffs:\n{0}'.format('\n'.join(diffs))

    def standardize_args(self):
        try:
            if type(self.actual) is unicode:
                self.actual = Helper.unicode_to_str(self.actual)
            if type(self.expected) is unicode:
                self.expected = Helper.unicode_to_str(self.expected)
        except NameError:
            pass

        if type(self.actual) is list:
            self.actual = Helper.unicode_list_to_str_list(self.actual)

        if type(self.expected) is list:
            self.expected = Helper.unicode_list_to_str_list(self.expected)


expect.register('eq', Equal)
expect.register('__eq__', Equal)

expect.register('ne', Equal, is_negative=True)
expect.register('__ne__', Equal, is_negative=True)
