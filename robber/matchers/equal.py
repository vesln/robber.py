from robber import expect
from robber.matchers.base import Base


class Equal(Base):
    """
    expect(1).to.eq(1)
    expect(1).to == 1
    expect(1) == 1
    """

    def matches(self):
        return self.actual == self.expected

    def failure_message(self):
        message = 'Expected {actual_type}("{actual_value}"){negative_message} ' \
                  'to equal {expected_type}("{expected_value}")'

        return message.format(
            actual_type=type(self.actual).__name__,
            actual_value=self.actual,
            negative_message=self.negative_message,
            expected_type=type(self.expected).__name__,
            expected_value=self.expected,
        )

expect.register('eq', Equal)
expect.register('__eq__', Equal)

expect.register('ne', Equal, is_negative=True)
expect.register('__ne__', Equal, is_negative=True)
