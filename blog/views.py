from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

from .models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = '__all__' # por montar um formulario, eh possivel passar uma lista de campos a serem enviados para o template 

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ('title', 'content', 'slug', 'status',)


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')