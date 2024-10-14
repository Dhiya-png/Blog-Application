from django.forms import forms,ModelForm
from django import forms
from django.contrib.auth.models import User

# sign up form

class registrationform(forms.ModelForm):
    password = forms.CharField(label = 'password',widget = forms.PasswordInput)
    cpassword = forms.CharField(label ='cpassword',widget = forms.PasswordInput)
    image = forms.ImageField(label = 'image')
    class Meta:
        model = User
        fields = ['username','email','password','cpassword','image']