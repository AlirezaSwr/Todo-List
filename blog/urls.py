from django.urls import path
from .views import Home, Detail, Delete, CreateTodo, UpdateTodo

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('detail/<int:pk>', Detail.as_view(), name='detail'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
    path('create/', CreateTodo.as_view(), name='create'),
    path('update/<int:pk>', UpdateTodo.as_view(), name='update'),
]
