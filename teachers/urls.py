from django.urls import path
from . import views

urlpatterns = [
    path('schedules/', views.schedule_list, name='schedule_list'),
    path('schedules/create/', views.schedule_create, name='schedule_create'),
    path('schedules/update/<int:pk>/', views.schedule_update, name='schedule_update'),
]
