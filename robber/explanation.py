class Explanation:
    def __init__(self, a, is_negative, action, b=None, c=None, additional_info=None):
        self.a = a
        self.action = action
        self.b = b
        self.c = c

        self.additional_info = '{0}\n'.format(additional_info) if additional_info else ''
        self.negative_word = ' not' if is_negative else ''
        self.b_word = ' B' if b else ''

    @property
    def message(self):
        return (
            '\n'
            '{line_a}'
            '{line_b}'
            '{line_c}'
            'Expected A{negative_word} to {action}{b_word}\n'
            '{additional_info}'
        ).format(
            line_a=self.build_line(self.a, 'A'),
            line_b=self.build_line(self.b, 'B'),
            line_c=self.build_line(self.c, 'C'),
            negative_word=self.negative_word,
            action=self.action,
            b_word=self.b_word,
            additional_info=self.additional_info
        )

    @staticmethod
    def build_line(obj, obj_name):
        if obj is not None:
            return '{obj_name} = {obj}\n'.format(
                obj_name=obj_name,
                obj=repr(obj)
            )
        return ''
