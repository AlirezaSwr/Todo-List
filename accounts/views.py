from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import CreatUserForm
from django.views.generic import CreateView



class UserCreate(SuccessMessageMixin, CreateView):
    template_name = 'userRegister.html'
    form_class = CreatUserForm
    success_url = reverse_lazy('home')
    success_message = 'User successfully created.'
