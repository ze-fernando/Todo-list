from django.urls import path
from .views import TaskDetailView, TaskListView


urlpatterns = [
    path('/<int:id>', TaskDetailView.as_view()),
    path('/', TaskListView.as_view())
]
