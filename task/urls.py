from django.urls import path
from .views import TaskDetail, TaskList


urlpatterns = [
    path('<int:id>', TaskDetail.as_view()),
    path('', TaskList.as_view())
]
