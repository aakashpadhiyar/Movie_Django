from django.urls import path
from .views import fetch_data_from_tr #Function
urlpatterns = [
    path('', fetch_data_from_tr, name='data'),
]
