from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
# Create your views here.

def Hello(request):
    return HttpResponse('Olá, Mundo!')

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class BlogCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ('title',  'content', 'category', 'image') # por montar um formulario, eh possivel passar uma lista de campos a serem enviados para o template 
    success_message = "%(field)s - alterados com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title,
        )

class BlogUpdateView(SuccessMessageMixin, LoginRequiredMixin,  UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ('title', 'content', 'image', 'status', 'category')
    success_message = "%(field)s - criado com sucesso"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title,
        )


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')