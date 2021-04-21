from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class LoginForm(forms.ModelForm):
    username = forms.CharField(label="الاسم")
    password = forms.CharField(label= "كلمه المرور", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username' , 'password']



class RegisterForm(UserCreationForm):
    username = forms.CharField(label="الاسم")
    email = forms.EmailField(label="الايميل")
    password1 = forms.CharField(label= "كلمه المرور", widget=forms.PasswordInput)    
    password2 = forms.CharField(label= "تاكيد كلمه المرور", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
    


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user' , 'slug' , 'created_at']


