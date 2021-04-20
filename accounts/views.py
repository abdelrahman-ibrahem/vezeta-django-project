from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import Profile
from .forms import LoginForm , Register , UpdateProfile
from django.urls import reverse
from django.contrib.auth import authenticate , login , logout
# Create your views here.

def index(request):
    index = Profile.objects.all()
    return render(request , 'accounts/index.html' , {
        'doctor':index
    })


def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username ,password=password)
        if user is not None :
            login(request , user)
            return HttpResponseRedirect(reverse('accounts:index'))

    else:
        form = LoginForm()
    return render(request , 'accounts/login.html' , {
        "form":form
    })


def signup(request):
    if request.method == 'POST':
        form2 = Register(request.POST)
        if form2.is_valid():
            form2.save()
            username = form2.cleaned_data['username']
            password = form2.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request , user)
                return HttpResponseRedirect(reverse('accounts:index'))
    else:
        form2 = Register()
    return render(request , 'accounts/signup.html' , {
        'forms':form2
    })


def doctor_details(request , slug):
    doctors =  Profile.objects.get(slug=slug)
    return render(request , 'accounts/doctors_detail.html' , {
        'detail':doctors
    })



def profile_page(request):
    return render(request , 'accounts/profile.html' , {

    })




def update_profile_page(request):
    if request.method == 'POST':
        update = UpdateProfile(request.POST , request.FILES , instance=request.user )
        if update.is_valid():
            update.save()
    else:
        update = UpdateProfile()
    return render(request , 'accounts/updata_profile.html' , {
        'update':update
    })



def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:index'))
