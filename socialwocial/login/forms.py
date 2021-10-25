from django import forms
from django.forms.widgets import FileInput, NumberInput

class loginform(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

class registerform(forms.Form):
    realname = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "id":"realname",
                "class":"wio-3"
                }))
    password = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'id':"password", "class":"wio-3"}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'id':"phonenumber", "class":"wio-3"}))
    profilepic = forms.ImageField(widget=forms.FileInput(attrs={'id':"profilepicture", "style":"opacity:0;"}))
    emailid = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'id':"emailid", "class":"wio-3"}))
    quailification = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id':"qualification", "class":"wio-3"}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'id':"dateofbirth", "class":"wio-3"}))
    idname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'id':"idname", "class":"wio-3"}))
    banner_image = forms.ImageField(widget=forms.FileInput(attrs={'id':"bannerimage", "class":"wio-3"}))