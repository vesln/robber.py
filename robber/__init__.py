import sys

# Do not change the importing order in the next 4 lines. Doing so may break everything.
from robber.custom_explanation import CustomExplanation  # noqa F401
from robber.expect import expect  # noqa F401
from robber.bad_expectation import BadExpectation  # noqa F401
import robber.matchers  # noqa F401

__all__ = [
    'custom_explanation', 'expect', 'bad_expectations', 'matchers',
]

# This hides the traceback
sys.tracebacklimit = 0

# This checks if ipython is installed then hide the traceback from it
try:  # pragma: no cover
    import traceback
    from IPython.core.interactiveshell import InteractiveShell

    def showtraceback(self):
        traceback_lines = traceback.format_exception(*sys.exc_info())
        sys.stderr.write(traceback_lines[-1])

    InteractiveShell.showtraceback = showtraceback
except ImportError:  # pragma: no cover
    pass
