from django.contrib import admin
from django.urls import path,include
from api import views
import rest_framework
urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewstu/',views.StudentAPI),
    path('viewstu/<int:id>/',views.StudentAPI),
    path('auth/',include('rest_framework.urls'))

]
