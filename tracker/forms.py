from django import forms

from tracker.models import Project, Task


class ProjectEditForm(forms.ModelForm):
    """
    редагування та реєстрація клієнта
    """
    class Meta:
        model = Project
        fields = "__all__"


class TaskForm(forms.ModelForm):
    """
    редагування та реєстрація клієнта
    """

    class Meta:
        model = Task
        exclude = ('created', 'modified', 'author')


