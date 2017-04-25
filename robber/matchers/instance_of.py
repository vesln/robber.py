from robber import expect
from robber.matchers.base import Base


class InstanceOf(Base):
    """
    expect(obj).to.be.an.instance_of(Klass)
    """

    def matches(self):
        return isinstance(self.actual, self.expected)

    def failure_message(self):
        return 'Expected "{actual}"{negative_message} to be an instance of "{expected}"'.format(
            actual=self.actual, negative_message=self.negative_message, expected=self.expected
        )


expect.register('instance_of', InstanceOf)
