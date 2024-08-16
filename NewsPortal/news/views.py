from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    # queryset = Post.objects.filter(post_type='News')
    model = Post
    template_name = 'news/posts.html'
    context_object_name = 'posts'

    ordering = 'add_date'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetails(DetailView):
    model = Post
    template_name = 'news/post_detailed.html'
    context_object_name = 'post'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['time_now'] = datetime.utcnow()
    #     context['next_sale'] = "Распродажа в среду!"
    #     return context


class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_create.html'

    raise_exception = True
    permission_required = ('news.add_post',)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_create.html'

    raise_exception = True
    permission_required = ('news.change_post',)


class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'news/post_delete.html'
    success_url = reverse_lazy('news')

    raise_exception = True
    permission_required = ('news.delete_post',)


def index(request):
    return render(request, 'news/index.html')


def news(request):
    obj = Post.objects.all()
    return render(request, 'news/posts.html', {'posts': obj})
