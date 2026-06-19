from django.urls import path
from . import views

urlpatterns = [

    path(
        'project/create/',
        views.create_project,
        name='create_project'
    ),
    path(
    'projects/',
    views.browse_projects,
    name='browse_projects'
    ),

    path(
    'project/<int:project_id>/',
    views.project_detail,
    name='project_detail'
    ),
    path(
    'project/<int:project_id>/apply/',
    views.apply_to_join,
    name='apply_to_join'
    ),

    path(
    'dashboard/',
    views.dashboard,
    name='dashboard'
    ),

    path(
    'request/<int:request_id>/accept/',
    views.accept_request,
    name='accept_request'
    ),

    path(
    'request/<int:request_id>/reject/',
    views.reject_request,
    name='reject_request'
    ),
]