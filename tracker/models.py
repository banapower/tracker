from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from tracker.utils.models import TextField
from user.models import User


class Project(models.Model):
    class Meta:
        db_table = 'project'

    name = models.CharField('Текст', max_length=50)
    description = TextField('Текст', blank=True)
    url = models.CharField('URL адреса', max_length=50, unique=True)
    programers = models.ManyToManyField(User)


class Task(models.Model):
    class Meta:
        db_table = 'task'

    TASK_TYPE_CHOICES = ((1, 'Фіча'),
                         (2, 'Баг'))

    TASK_PRIORITY_CHOICES = ((1, 'нормальний'),
                             (2, 'високій'),
                             (3, 'срочно'))

    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.PROTECT)
    topic = models.CharField('Тема', max_length=100)
    description = models.CharField('Опис', max_length=255)
    date_from = models.DateTimeField('Дата початку')
    date_to = models.DateTimeField('Дата закінчення')
    type = models.IntegerField('Тип', choices=TASK_TYPE_CHOICES)
    priority = models.IntegerField('Пріоритет', choices=TASK_PRIORITY_CHOICES)
    estimated_time = models.PositiveIntegerField('Оціночний час в годинах')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks', on_delete=models.PROTECT)
    performer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks_to_do', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    class Meta:
        db_table = 'comment'

    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey('content_type', 'object_id')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.PROTECT)
    text = models.CharField('Текст', max_length=255)
    created = models.DateTimeField(auto_now_add=True)


class TimeLogging(models.Model):
    class Meta:
        db_table = 'time_logging'

    spent_time = models.PositiveIntegerField('Витрачений час в годинах')
    task = models.ForeignKey(Task, on_delete=models.PROTECT)

