from django.urls import path
from.views import UserCreate

urlpatterns = [
    path('', UserCreate.as_view(), name='User_registration'),
]