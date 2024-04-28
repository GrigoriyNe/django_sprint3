from django.shortcuts import render
from django.http import Http404



def index(request):
    template = 'blog/index.html'
    context = {'post': posts, 'flag': 'true'}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    try:
        post_id in post_dict
        context = {'post': post_dict[post_id]}
    except KeyError:
        raise Http404(f'Страница "{post_id}" не найдена')
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'post': category_slug}
    return render(request, template, context)
