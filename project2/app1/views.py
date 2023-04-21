from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    html = '<html><body><h1>Hello, world!</h1></body></html>'
    return render(request, 'index.html')