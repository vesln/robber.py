from robber import expect

class failure_message():
    """
    with failure_message('Custom failure message'):
        # some assertions
    """
    def __init__(self, message):
        self.message = message

    def __enter__(self, *args, **kwargs):
        expect.fail_with(self.message)

    def __exit__(self, *args, **kwargs):
        expect.remove_custom_message()

