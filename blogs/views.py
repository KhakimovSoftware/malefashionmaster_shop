from django.shortcuts import render
from .models import PostModel
from django.views.generic import ListView, DetailView

class PostListView(ListView):
    queryset = PostModel.objects.order_by('-id')
    template_name = 'blog.html'


class PostDetailView(DetailView):
    model = PostModel
    template_name = 'blog-detail.html'