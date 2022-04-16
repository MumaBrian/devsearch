from os import name
from django.urls import URLPattern, path 
from . import views
urlpatterns =[
path('',views.projects,name='projects'),
path('project/<str:pk>/',views.project,name='project'),
path('createproject',views.createProject,name='createproject'),
path('updateproject/<str:pk>/',views.updateProject,name='updateproject'),
path('deleteproject/<str:pk>/',views.deleteProject,name='deleteproject'),
]
