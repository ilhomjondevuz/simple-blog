from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blogapp/post_list.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogapp/blog_detail.html'
    context_object_name = 'post'