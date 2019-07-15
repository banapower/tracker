from django import forms
from tracker.models import Project, Task, Comment, TimeLogging


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
    date_from = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        exclude = ('created', 'modified', 'author', 'project')


class CommentAddForm(forms.ModelForm):
    """
    створення коментара
    """
    class Meta:
        model = Comment
        fields = ('text', )


class TimeLoggingForm(forms.ModelForm):
    """
    створення логування часу
    """
    class Meta:
        model = TimeLogging
        fields = ('spent_time', 'comment')
