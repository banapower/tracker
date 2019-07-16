from django.core import exceptions
from django.db import models
from tracker.utils.forms import Textarea


class TextField(models.TextField):

    def formfield(self, **kwargs):
        defaults = {'widget': Textarea}
        defaults.update(kwargs)
        return super(TextField, self).formfield(**defaults)


class SlugField(models.CharField):

    def clean(self, value, obj):
        try:
            value.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            raise exceptions.ValidationError('Поле повинне містити Тільки англійські літери')
        return super(SlugField, self).clean(value, obj)
