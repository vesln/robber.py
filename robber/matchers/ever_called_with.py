from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base
from robber.matchers.mock_mixin import MockMixin


class EverCalledWith(Base, MockMixin):
    """
    expect(mock).to.have.been.ever_called_with(*args, **kwargs)
    expect(mock).to.have.any_call(*args, **kwargs)
    """

    def matches(self):
        try:
            return self.call_args in self.actual.call_args_list
        except AttributeError:
            raise TypeError('{actual} is not a mock'.format(actual=self.actual))

    @property
    def explanation(self):
        return Explanation(
            self.actual, self.is_negative, 'have been ever called with', self.expected_args_str,
            force_disable_repr=True
        )


expect.register('ever_called_with', EverCalledWith)
expect.register('any_call', EverCalledWith)
