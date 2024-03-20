from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

# Create your views here.

def home(request):
    
    return render(request,'authentication/index.html')


def signup(request):
    
    if request.method == 'POST':
        username=request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
        
        my_user=User.objects.create_user(username,email,pass1)
        my_user.first_name= fname
        my_user.last_name= lname
        
        print(my_user)
        my_user.save()
        
        messages.success(request,'your account has been succefully created')
        
        return redirect('signin')
        
        
    
    return render(request,'authentication/signup.html')


def signin(request):
    
    if request.method == 'POST':
        
        username=request.POST['username']
        pass1   =request.POST['pass1']
        
        user=authenticate(username=username, password=pass1)
        if user is not None:
            login(request,user)
            
            fname=user.first_name
            
            return render(request,'authentication/index.html',{'fname':fname})
            
        else:
            messages.error(request,'Bad Credentials')
            return redirect('home')
    
    return render(request,'authentication/sigin.html')


def signout(request):
    
   logout(request)
   messages.success(request,'you have been logged out')
   
   return redirect('home')
