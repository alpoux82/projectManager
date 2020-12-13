
from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.companies, name='company_list'),
    path('company/<int:pk>', views.company, name='company_detail'),
    path('billinginfolist/', views.billinginfolist, name='billinginfo_list'),
    path('billinginfo/<int:pk>', views.billinginfo, name='billinginfo_detail'),
    path('users/', views.users, name='user_list'),
    path('user/<int:pk>', views.user, name='user_detail'),
    path('projects/', views.projects, name='project_list'),
    path('project/<int:pk>', views.project, name='project_detail'),
    path('tasks/', views.tasks, name='task_list'),
    path('task/<int:pk>', views.task, name='task_detail'),
    path('tags/', views.tags, name='tag_list'),
    path('tag/<int:pk>', views.tag, name='tag_detail'),
]