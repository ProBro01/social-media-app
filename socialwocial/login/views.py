from django.shortcuts import redirect, render, HttpResponse
from .forms import loginform

# Create your views here.
def index(request):
    form = loginform()
    return render(request, "index.html", {"form":form})
    # return HttpResponse("<h1>Login page</h1>")

def register(request):
    if request.method == 'GET':
        return render(request, "register.html")
    elif request.method == 'POST':
        return redirect('/profile')
        return HttpResponse("<h1>Register page</h1>")

def resetpasswd(request):
    return HttpResponse("<h1>Reset password </h1>")