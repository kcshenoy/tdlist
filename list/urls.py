from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="tasks"),
    path('update_tasks/<str:primkey>/', views.update_task, name='update_task'),
    path('delete/<str:primkey>/', views.delete_tasks, name='delete')
]