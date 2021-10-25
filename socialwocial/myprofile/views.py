from django.http.response import HttpResponse
from django.shortcuts import render
from login.models import users

# Create your views here.
def index(request):
    return HttpResponse("<h1>Profile page</h1>")