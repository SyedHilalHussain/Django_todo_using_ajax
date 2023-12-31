from django.urls import path
from .import views

urlpatterns =[
    path('', views.apiOverview, name="api-Overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.detailList, name="task-detail"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
   
    path('task-create/', views.taskcreate, name="task-create"),
    
] 