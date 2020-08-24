from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('task/', views.tasks, name='task'),
    path('add_task/', views.addtask, name='add_task'),
    path('update_task/<int:pk>', views.updatetask, name='update_task'),
    path('delete_task/<int:pk>/', views.deletetask, name='delete_task'),
    path('', include('register.urls')),
    # path('complete_task/<int:pk>/', views.completetask, name='complete_task')


]
