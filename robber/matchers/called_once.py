from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class CalledOnce(Base):
    """
    expect(mock).to.be.called_once()
    """

    def matches(self):
        try:
            return self.actual.call_count == 1
        except AttributeError:
            raise TypeError('{actual} is not a mock'.format(actual=self.actual))

    @property
    def explanation(self):
        return Explanation(
            self.actual, self.is_negative, 'be called once',
            more_detail='Called {0} times'.format(self.actual.call_count)
        )


expect.register('called_once', CalledOnce)
