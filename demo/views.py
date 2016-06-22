from django.shortcuts import render

from .models import Post


def index_gargoyle(request):
    """
    Example of usage Gargoyle feature flags
    """
    context = {'posts': Post.objects.all()}
    return render(request, 'demo/index.html', context)


def index_waffle(request):
    """
    Example of usage Waffle feature flags
    """
    context = {'posts': Post.objects.all()}
    return render(request, 'demo/index.html', context)
