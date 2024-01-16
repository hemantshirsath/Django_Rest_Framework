from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stulist/',views.StudentList.as_view()),
    path('stucreate/',views.StudentCreate.as_view()),
    path('stuupdate/<int:pk>/',views.StudentUpdate.as_view()),
    path('sturetrieve/<int:pk>/',views.StudentRetrieve.as_view()),
    path('studelete/<int:pk>/',views.StudentDelete.as_view()),
    path('stulistcreate/',views.StudentListCreate.as_view()),
    path('sturetrieveupdate/<int:pk>/',views.StudentRetrieveUpdate.as_view()),
    path('sturetrievedelete/<int:pk>/',views.StudentRetrieveDestroy.as_view()),
    path('sturetrieveupdatedelete/<int:pk>/',views.StudentRetrieveUpdateDelete.as_view())
]
