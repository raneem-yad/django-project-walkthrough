from django.http import HttpResponse
from django.shortcuts import render

from about.models import About


# Create your views here.
def about(request):
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about.html",
        {"about": about},
    )
