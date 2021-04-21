from django.urls import path 
from . import views
app_name = 'accounts'
urlpatterns = [
    path('' , views.index , name="index"),
    path('login/' , views.signin , name="login" ),
    path('register/' , views.signup , name="register" ),
    path('my_profile' , views.profile_page , name="profile"),
    path('logout/' , views.logout_page , name="logout"),
    path('doctor_details/<str:slug>/' , views.doctor_details , name="doctor_details"),
]