from django.conf import settings

from django.shortcuts import get_object_or_404, render

from blog.models import Category, Post


published_list = Post.published.all().select_related("author")


def index(request):
    template = "blog/index.html"
    post_list = published_list.order_by("title")[: settings.POSTS_ON_PAGE]
    context = {"post_list": post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = "blog/detail.html"
    posts = get_object_or_404(published_list.filter(pk=pk))
    context = {"post": posts}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = "blog/category.html"
    category = get_object_or_404(
        Category.objects.filter(is_published=True, slug=category_slug)
    )
    post_list = category.posts(manager="published").all()
    context = {"category": category, "post_list": post_list}
    return render(request, template, context)
