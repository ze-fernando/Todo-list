from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('task.urls')),
    path('user/', include('user.urls')),
]
