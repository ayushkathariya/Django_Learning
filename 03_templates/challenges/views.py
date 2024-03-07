from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "challenges/index.html")


def contact(request):
    return render(request, "challenges/contact.html")


def about(request):
    return render(request, "challenges/about.html")


def template(request):
    return render(request, "challenges/template.html")
