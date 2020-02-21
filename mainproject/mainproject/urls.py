
from django.contrib import admin
from django.urls import path, include
import mainapp.views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp.views.home,name="home"),
    path('user/', include('user.urls')),
]
