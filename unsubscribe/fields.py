import uuid

from django.core import exceptions
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UUIDField(models.CharField):
    default_error_messages = {
        'invalid': _('Enter a valid UUID.'),
    }

    def prepare_value(self, value):
        if isinstance(value, uuid.UUID):
            return str(value)
        return str(value)

    def to_python(self, value):
        value = super(UUIDField, self).to_python(value)
        if value in self.empty_values:
            return None
        if not isinstance(value, uuid.UUID):
            try:
                value = uuid.UUID(value)
            except ValueError:
                raise exceptions.ValidationError(self.error_messages['invalid'], code='invalid')
        return value.hex
