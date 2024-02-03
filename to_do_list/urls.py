from django.urls import path
from . import views


urlpatterns = [
    path('task_list/', views.task_list_api_view),
    path('task_list/<int:id>/', views.task_detail_api_view),
    path('task_create/', views.task_create_api_view),
]
