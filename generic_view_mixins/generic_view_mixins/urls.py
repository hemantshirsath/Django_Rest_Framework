from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('liststu/',views.StudentList.as_view()),
    path('retrivestu/<int:pk>',views.StudentRetrieve.as_view()),
    path('createstu/',views.StudentCreate.as_view()),
    path('updatestu/<int:pk>/',views.studentUpdate.as_view()),
    path('deletestu/<int:pk>/',views.studentDelete.as_view())
]
