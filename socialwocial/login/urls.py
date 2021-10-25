from django.urls import path
from login import views

urlpatterns = [
    path("", views.index, name='loginmain'),
    path("register/", views.register, name='registerpage'),
    path("resetpass/", views.resetpasswd, name='passwordreset')
]