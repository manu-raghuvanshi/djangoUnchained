from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homePageView(request) -> HttpResponse:
    return HttpResponse("Hello, World!")