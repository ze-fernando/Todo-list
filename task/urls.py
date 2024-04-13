from django.urls import path
from .views import TaskDetail, TaskList


urlpatterns = [
    path('<int:id>', TaskDetail.as_view(), name='detail'),
    path('', TaskList.as_view(), name='list')
]
