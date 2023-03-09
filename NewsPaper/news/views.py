from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import PostForm
from .models import Post, Category
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = '-creating_dt'
    template_name = 'news/news.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/new.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'


class PostDelete(DeleteView):

    form_class = PostForm
    model = Post
    template_name = 'news/post_delete.html'


class CategoryList(ListView):
    model = Post
    template_name = 'news/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-creating_dt')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscriber.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscriber.add(user)

    message = f'Вы успешно подписались на рассылку новостей из категории.'
    return render(request, 'news/subscribe.html', {'category': category, 'message': message})

