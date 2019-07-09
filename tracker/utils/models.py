from django.db import models
from tracker.utils.forms import Textarea


class TextField(models.TextField):

    def formfield(self, **kwargs):
        defaults = {'widget': Textarea}
        defaults.update(kwargs)
        return super(TextField, self).formfield(**defaults)
