from django.shortcuts import render


def top(request):
    """ トップページ """
    template_name = "home.html"

    return render(request, template_name)
