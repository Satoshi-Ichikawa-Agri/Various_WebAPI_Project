from django.shortcuts import render


def top(request):
    """ トップページ """
    template_name = 'base.html'

    return render(request, template_name)
