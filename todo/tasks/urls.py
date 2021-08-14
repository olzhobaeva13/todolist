from django.urls import path
from .views import TaskAPIView, TaskDetailAPIView, TaskFinishedAPIView

urlpatterns = [
    path('tasks/', TaskAPIView.as_view(), name='task_list_url'),
    path('tasks/<int:id>/', TaskDetailAPIView.as_view(), name='task_detail_url'),
    path('tasks/finished/<int:id>/', TaskFinishedAPIView.as_view(), name='task_finished_url')
]