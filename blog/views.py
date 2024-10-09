from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import PostForm
from .models import Post


"""
FBV - Function based views (Предстовления основоных на функциях)
CBV - Class based views (Предстовление основаных на классах)
"""

def root(request):
    return render(request, template_name='blog/index.html')


def index(request):
    return render(request, template_name='blog/index.html')


def about(request):
    context = {
        'name': 'Дмитрий',
        'lastname': 'Горим',
        'email': 'd.gorin@mail.ru',
        'title': 'О сайте'
    }
    return render(request, template_name='blog/about.html', context=context)

@login_required
def add_post(request):
    if request.method == "GET":
        form = PostForm(author=request.user)
        context = {
            'form': form,
            'title': 'Добовления поста'
        }
        return render(request, template_name='blog/add_post.html', context=context)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, author=request.user)
        if form.is_valid():
            form.save()

        return index(request)


def post_list(request):
    # Получаем все объект модели Post
    # Сортируем по убыванию
    posts = Post.objects.all().order_by('-created_at')
    # Показываем по 3 поста на странице
    paginator = Paginator(posts, 3)
    # Получаем номмер страницы из url
    page_number = request.GET.get('page')
    # Получаем объекты для текущей страницы
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Посты',
        'page_obj': page_obj
    }
    return render(request, template_name='blog/posts.html', context=context)


def post_detail(request, slug):
    # Получаем объект с задоным pk(ключем)
    post = get_object_or_404(Post, slug=slug)
    context = {
        'title': 'Информация о посте',
        'post': post
    }
    return render(request, template_name='blog/post_detail.html', context=context)

@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return post_list(request)

    else:
        form = PostForm(instance=post)

    context = {
        'forma': form,
        'title': 'Редактировать пост'
    }
    return render(request, template_name='blog/post_edit.html', context=context)

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_list')
    return render(request, template_name='blog/post_delete.html', context={'post': post})

def page_not_found(request, exception):
    return render(request, 'blog/404.html', status=404)

def forbidden(request, exception):
    return render(request, 'blog/403.html', status=403)

def server_error(request):
    return render(request, 'blog/500.html', status=500)