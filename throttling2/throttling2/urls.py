from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentlist/',views.StudentList.as_view()),
    path('studentretrieve/<int:pk>/',views.StudentRetrieve.as_view()),
    path('studentCreate/',views.StudentCreate.as_view()),
    path('',include('rest_framework.urls'))
]
