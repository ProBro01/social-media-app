from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Login page</h1>")

def register(request):
    return HttpResponse("<h1>Register page</h1>")

def resetpasswd(request):
    return HttpResponse("<h1>Reset password </h1>")