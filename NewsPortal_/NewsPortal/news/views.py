from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class PostList(ListView):
    # queryset = Post.objects.filter()
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'news'

    ordering = 'add_date'


class PostDetails(DetailView):
    model = Post
    template_name = 'news/unit_of_news.html'
    context_object_name = 'unit_of_news'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['time_now'] = datetime.utcnow()
    #     context['next_sale'] = "Распродажа в среду!"
    #     return context


def index(request):

    return render(request, 'news/index.html')


def news(request):
    obj = Post.objects.all()
    return render(request, 'news/news.html', {'news': obj})
