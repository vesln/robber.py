from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base
from robber.matchers.mock_mixin import MockMixin


class CalledWith(Base, MockMixin):
    """
    expect(mock).to.be.called_with(*args, **kwargs)
    """

    def matches(self):
        try:
            return self.actual.called and self.actual.call_args == self.call_args
        except AttributeError:
            raise TypeError('{actual} is not a mock'.format(actual=self.actual))

    @property
    def explanation(self):
        if not self.actual.called:
            return Explanation(
                self.actual, self.is_negative, 'be called with', self.expected_args_str,
                more_detail='Actually not called', force_disable_repr=True
            )

        return Explanation(
            self.actual, self.is_negative, 'be called with', self.expected_args_str,
            other=self.call_args_str, force_disable_repr=True
        )


expect.register('called_with', CalledWith)
