from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect

from tracker.forms import ProjectEditForm, TaskForm
from tracker.models import Project, Task
from tracker.utils.utils import close_view


def index(request):
    print(request.user)
    if request.user.is_authenticated:
        return redirect('project-list')
    return redirect('login')


def project_list(request):
    user = request.user
    if user.is_staff:
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(programers=user)
        print(projects)
    return render(request, 'project_list.html', {'projects': projects})


def priject_show(request, url):
    project = get_object_or_404(Project, url=url, programers=request.user)
    print(project.tasks.all())
    return render(request, 'project_show.html', {'project': project})


@user_passes_test(lambda u: u.is_staff)
def project_edit(request, url):
    project = None if url == '0' else get_object_or_404(Project, url=url)
    form = ProjectEditForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return close_view(request, 'project-list')
    return render(request, 'project_edit.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def project_task_edit(request, url, pk):
    task = None if pk == '0' else get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        task = form.save(commit=False)
        task.author = request.user
        task.save()
    return render(request, 'login.html', {'form': form})

