# notifications/urls.py
from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.notification_list, name='list'),
    path('api/count/', views.notification_count_api, name='count_api'),
    path('api/dropdown/', views.notification_dropdown_api, name='dropdown_api'),
    path('<int:pk>/read/', views.mark_as_read, name='mark_read'),
    path('<int:pk>/delete/', views.delete_notification, name='delete'),
    path('read-all/', views.mark_all_read, name='mark_all_read'),
    path('delete-selected/', views.delete_selected, name='delete_selected'),
    path('delete-all/', views.delete_all, name='delete_all'),
]
