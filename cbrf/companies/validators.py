class MinValueValidator(BaseValidator):
    message = _('Ensure this value is greater than or equal to %(limit_value)s.')
    code = 'min_value'
    def compare(self, a, b):
        return a <= b
