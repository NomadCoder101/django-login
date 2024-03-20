from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('my-login',views.my_login,name="my_login"),
    path('logout',views.user_logout,name="logout"),
    path('dashboard',views.dashboard,name="dashboard"),
    
   
]
