from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('GetData/', include('GetData.urls')),
    path('', include('HTML.urls')),
    path('admin/', admin.site.urls),
]
