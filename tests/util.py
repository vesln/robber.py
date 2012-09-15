from robber import BadExpectation

def must_fail(fn, *args, **kwargs):
    def test_decorated(self, *args, **kwargs):
        try:
            fn(self, *args, **kwargs)
        except BadExpectation:
            pass
        else:
            raise BadExpectation, 'it must fail'

    return test_decorated

