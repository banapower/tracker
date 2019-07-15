from django.contrib.auth.decorators import user_passes_test, login_required
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from tracker.forms import ProjectEditForm, TaskForm, CommentAddForm, TimeLoggingForm
from tracker.models import Project, Task, Comment
from tracker.utils.utils import close_view, cmp_to_text, compare


def index(request):
    """
    redirect user to correct url
    """
    if request.user.is_authenticated:
        return redirect('project-list')
    return redirect('login')


def project_list(request):
    """
    view projects related to user or is user stuff view all projects
    """
    user = request.user
    if user.is_staff:
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(programers=user)
    return render(request, 'project_list.html', {'projects': projects})


@login_required
def project_show(request, url):
    project = get_object_or_404(Project, url=url, programers=request.user)
    return render(request, 'project_show.html', {'project': project})


@user_passes_test(lambda u: u.is_staff)
def project_edit(request, url):
    project = None if url == '0' else get_object_or_404(Project, url=url)
    form = ProjectEditForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return close_view(request, 'project-list')
    return render(request, 'project_edit.html', {'form': form})


@login_required
def project_task_show(request, url, pk):
    """
    show task and add comments
    """
    project = get_object_or_404(Project, url=url, programers=request.user)
    task = get_object_or_404(Task, pk=pk, project=project)
    comment_add_form = CommentAddForm(request.POST or None)
    task_time = task.time_logging.all().aggregate(Sum('spent_time'))['spent_time__sum']
    if comment_add_form.is_valid():
        comment = comment_add_form.save(commit=False)
        comment.task = task
        comment.author = request.user
        comment.save()
        return redirect('project-task-show', url, pk)
    return render(request, 'task_show.html', {'task': task, 'comment_add_form': comment_add_form,
                                              'task_time': task_time})


def project_task_edit(request, url, pk):
    """
    edit task and send email
    """
    user = request.user
    project = get_object_or_404(Project, url=url,  programers=user)
    task = None if pk == '0' else get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    task_before = dict(task.__dict__) if task else {}
    if form.is_valid():
        task = form.save(commit=False)
        task.author = request.user
        task.project = project
        task.save()
        task_after = dict(task.__dict__)
        changes = cmp_to_text(compare(task_before, task_after, exclude=['modified']))
        message = '\n'.join(changes)
        print('>>>> send mail >>>>', message)
        # send_mail('Редагування задачі', 'Будл змфнено %s' % message, 'from@example.com', ['to@example.com'],
        #           fail_silently=False)
        return close_view(request, 'project-show', project.url)
    return render(request, 'task_edit.html', {'form': form})


@login_required
def time_logging_edit(request, url, pk):
    user = request.user
    task = get_object_or_404(Task, pk=pk, project__url=url, performer=user)
    tiam_logging_form = TimeLoggingForm(request.POST or None)
    if tiam_logging_form.is_valid():
        time_logging = tiam_logging_form.save(commit=False)
        time_logging.task = task
        time_logging.save()
        return close_view(request, 'project-task-show', task.project.url, task.pk)
    return render(request, 'time_logging_edit.html', {'time_logging_form': tiam_logging_form})


