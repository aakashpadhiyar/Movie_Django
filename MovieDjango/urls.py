from django.contrib import admin
from django.urls import path, include
from django.urls import path
from rest_framework_app.views import *


app_name = 'rest_framework_app'

urlpatterns = [
    path('GetData/', include('GetData.urls')),
    path('api-auth/', include('rest_framework_app.urls')),
    path('admin/', admin.site.urls),
]
