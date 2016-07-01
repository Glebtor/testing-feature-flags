import waffle
from gargoyle import gargoyle

from django.shortcuts import render

from telega_feature_flag.feature_flags import FRONTEND_TITLE_FEATURE, NAZI_FEATURE


def index_gargoyle(request):
    """
    Example of usage Gargoyle feature flags
    """
    context = {
        'title': 'Regular title',
    }
    if gargoyle.is_active(FRONTEND_TITLE_FEATURE, request):
        context.update({'title': 'Fancy title enabled by feature flag'})

    return render(request, 'playground/index_gargoyle.html', context)


def index_waffle(request):
    """
    Example of usage Waffle feature flags
    """
    context = {'title': 'Regular title'}
    if waffle.flag_is_active(request, 'title_feature'):
        context.update({'title': 'Fancy title enabled by feature flag'})

    return render(request, 'playground/index_waffle.html', context)
