
from django.contrib import admin
from django.urls import path
from api.views import create_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createstu/',create_student)
]
