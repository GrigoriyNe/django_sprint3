from django.shortcuts import render
from blog.models import Post, Category
from django.shortcuts import get_object_or_404


def index(request):
    template = 'blog/index.html'
    post_list = (Post.objects.select_related(
        'category')
    ).filter(
        is_published=True)[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    posts = get_object_or_404(
        Post.objects.filter(is_published=True),
        pk=post_id
    )
    context = {'post': posts}

    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )

    post_list = Post.objects.filter(
        is_published=True, 
        category__slug=category_slug
        )
    
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
