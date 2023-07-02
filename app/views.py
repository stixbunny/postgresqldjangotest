from django.shortcuts import render
from .models import Film


def index(request):
    context = {"films": Film.objects.all()}
    return render(request, "index.html", context=context)
