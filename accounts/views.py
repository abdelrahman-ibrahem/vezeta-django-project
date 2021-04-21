from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import Profile
from .forms import LoginForm , RegisterForm , UpdateProfile
from django.urls import reverse
from django.contrib.auth import authenticate , login , logout
from .filter import Filter
from django.core.paginator import Paginator
# Create your views here.


# fucntion  home page 
def index(request):
    index = Profile.objects.all()
    # filter 
    myFliter = Filter(request.GET , queryset=index)
    index = myFliter.qs
    paginator = Paginator(index , 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request , 'accounts/index.html' , {
        'doctor':page_obj , 'filter':myFliter
    })


# function login page
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

# function to register in this website 
def signup(request):
    if request.method == 'POST':
        form2 = RegisterForm(request.POST)
        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect(reverse('accounts:login'))
            # username = form2.cleaned_data['username']
            # password = form2.cleaned_data['password1']
            # user = authenticate(username=username , password=password)
            # if user is not None:
            #     login(request , user)
            #     return HttpResponseRedirect(reverse('accounts:index'))
    else:
        form2 = RegisterForm()
    return render(request , 'accounts/signup.html' , {
        'forms':form2
    })


# function to display doctor information
def doctor_details(request , slug):
    doctors =  Profile.objects.get(slug=slug)
    return render(request , 'accounts/doctors_detail.html' , {
        'detail':doctors
    })


# function to display your profile
def profile_page(request):
    return render(request , 'accounts/profile.html' , {

    })



#function to update profile page
def update_profile_page(request):
    if request.method == 'POST':
        update = UpdateProfile(request.POST , request.FILES , instance=request.user )
        if update.is_valid() :
            update.save()
            return HttpResponseRedirect(reverse('accounts:profile'))

    else:
        update = UpdateProfile()
    return render(request , 'accounts/updata_profile.html' , {
        'update':update
    })


# function to logout from this page 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:index'))
