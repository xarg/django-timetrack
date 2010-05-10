import re

from django import forms
from django.db import models

NUMERIC_PATTERN = re.compile('^\d+:\d{1,2}$')
ERROR_MESSAGE = 'Invalid input format. Accepted format: hhhh:mm'

class TimeSumField(models.CharField):
    def __init__(self, *args, **kwargs):
        if 'max_length' not in kwargs:
            kwargs['max_length'] = 10
        super(TimeSumField, self).__init__(*args, **kwargs)
    def validate(self, value, object = None):
        "Check if value is hhhhhh:mm format"
        # Use the parent's handling of required fields, etc.
        super(TimeSumField, self).validate(value, object)
        
        if not NUMERIC_PATTERN.match(value):
            raise forms.ValidationError(ERROR_MESSAGE)
        try:
            time_sum = str(value).split(':')
            hours = int(time_sum[0])
            minutes = int(time_sum[1])
        except:
            raise forms.ValidationError(ERROR_MESSAGE)
        if minutes > 59:
            raise forms.ValidationError(ERROR_MESSAGE)