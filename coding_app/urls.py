# coding_quiz_app/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),  # Make sure this line is correct
]
