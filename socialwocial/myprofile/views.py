from django.http.response import HttpResponse
from django.shortcuts import render
from login.models import users

# Create your views here.
def index(request):
    '''
    if registeration request
        first create the user
        save the user
        return the profile page to him with his details
    if login request
        search the user and validate him
        them return the profile page to him with his details
    '''
    if request.method == 'POST':
        profiledetails = {}
        '''
        creating the user object
        '''
        for var in request.POST.items():
            profiledetails[var[0]] = var[1]
        userobject = users(
            realname = request.POST.get("realname"),
            password = request.POST.get("password"),
            phone = request.POST.get("phone"),
            emailid = request.POST.get("emailid"),
            quailification = request.POST.get("quailification"),
            dob = request.POST.get("dob"),
            idname = request.POST.get("idname"),
            profilepic = request.FILES.get('profilepic'),
            banner_image = request.FILES.get('banner_image')
        )
        userobject.save()
        return render(request, "profile.html")