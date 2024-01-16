
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('createstu/',views.create_student),
    path('createstu/<int:pk>/',views.create_student)
]
