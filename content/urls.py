from django.urls import path
from .views import project_list, experience_list

urlpatterns = [
    path('', project_list, name='project_list'),
    path('experience_list', experience_list, name='experience_list'),
]