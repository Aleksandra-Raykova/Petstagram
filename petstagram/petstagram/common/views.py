from django.shortcuts import redirect, render
from petstagram.common import view_mixins


def show_home_page(request):
    return render(request=request, template_name='common/home-page.html')
