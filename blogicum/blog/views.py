from django.shortcuts import render
from blog.models import Post, Category
from django.shortcuts import get_object_or_404
from django.conf import settings


published = Post.objects.published().select_related(
    'author')


def index(request):
    template = 'blog/index.html'
    post_list = published[:settings.POSTS_ON_PAGE]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    posts = get_object_or_404(
        published.filter(pk=pk))
    context = {'post': posts}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(
            is_published=True,
            slug=category_slug))
    post_list = published.filter(
        category__slug=category_slug)

    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
