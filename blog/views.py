from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Blog


class Home(ListView):
    model = Blog
    template_name = 'home.html'


class Detail(DetailView):
    model = Blog
    template_name = 'detail.html'


class Delete(DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


class CreateTodo(CreateView):
    model = Blog
    fields = ['title', 'caption', 'created']
    template_name = 'create.html'
    success_url = reverse_lazy('home')


class UpdateTodo(UpdateView):
    model = Blog
    fields = ['title', 'caption', 'created']
    template_name = 'update.html'
    success_url = reverse_lazy('home')
