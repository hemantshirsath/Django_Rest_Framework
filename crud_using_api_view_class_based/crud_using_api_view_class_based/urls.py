
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewstu/',views.StudentAPI.as_view()),
    path('viewstu/<int:pk>',views.StudentAPI.as_view())
]
