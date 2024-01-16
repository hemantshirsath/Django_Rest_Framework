from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_view_create/',views.StudentCreateview.as_view()),
    path('student_modify/<int:pk>/',views.StudentModify.as_view())
]
