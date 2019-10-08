from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):  # HttpRequest 타입
    message = "Welcome to the Django World."
    return HttpResponse("<h1>Hello</h1>" + message)
