from django.shortcuts import redirect, render, HttpResponse
from .forms import loginform, registerform

# Create your views here.
def index(request):
    form = loginform()
    return render(request, "index.html", {"form":form})
    # return HttpResponse("<h1>Login page</h1>")

def register(request):
    if request.method == 'GET':
        form = registerform()
        return render(request, "register.html", {"regform" : form})

def resetpasswd(request):
    return HttpResponse("<h1>Reset password </h1>")