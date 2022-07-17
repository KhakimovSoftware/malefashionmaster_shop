from django.shortcuts import render
from .models import PostModel
from django.views.generic import ListView, DetailView

class PostListView(ListView):
    template_name = 'blog.html'

    def get_queryset(self):
        qs = PostModel.objects.order_by('-id')
        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tag__name=tag)
        return qs


class PostDetailView(DetailView):
    model = PostModel
    template_name = 'blog-detail.html'