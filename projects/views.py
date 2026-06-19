from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm
from .models import Project, JoinRequest
from django.db.models import Q
from django.shortcuts import get_object_or_404


def create_project(request):

    if request.method == 'POST':

        form = ProjectForm(request.POST)

        if form.is_valid():

            project = form.save(commit=False)

            project.owner = request.user

            project.save()

            return redirect('/')

    else:

        form = ProjectForm()

    return render(
        request,
        'create_project.html',
        {'form': form}
    )


def browse_projects(request):

    query = request.GET.get('q')

    if query:

        projects = Project.objects.filter(
            Q(title__icontains=query)

            |

            Q(required_skills__icontains=query)

        )

    else:

        projects = Project.objects.all()

    return render(
        request,
        'browse_projects.html',
        {'projects': projects}
    )

def project_detail(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id
    )

    return render(
        request,
        'project_detail.html',
        {'project': project}
    )

def apply_to_join(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id
    )

    JoinRequest.objects.create(
        applicant=request.user,
        project=project
    )

    return redirect('browse_projects')

def dashboard(request):

    my_projects = Project.objects.filter(
        owner=request.user
    )

    applications_sent = JoinRequest.objects.filter(
        applicant=request.user
    )

    requests_received = JoinRequest.objects.filter(
        project__owner=request.user
    )

    return render(
        request,
        'dashboard.html',
        {
            'my_projects': my_projects,
            'applications_sent': applications_sent,
            'requests_received': requests_received
        }
    )

def accept_request(request, request_id):

    join_request = get_object_or_404(
        JoinRequest,
        id=request_id
    )

    if join_request.project.owner != request.user:
        return redirect('dashboard')

    join_request.status = 'accepted'

    join_request.save()

    return redirect('dashboard')


def reject_request(request, request_id):

    join_request = get_object_or_404(
        JoinRequest,
        id=request_id
    )

    if join_request.project.owner != request.user:
        return redirect('dashboard')

    join_request.status = 'rejected'

    join_request.save()

    return redirect('dashboard')