
from django.contrib import admin
from django.urls import path
from api import views
from api2 import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>',views.view_student,name="view_student"),
    path('stuinfo/',views.viewall,name="all"),
    path("createstu/",v.create_student)
]
