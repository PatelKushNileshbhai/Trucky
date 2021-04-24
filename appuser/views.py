from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from .models import *


# Create your views here.

def AboutUS(request):
    return render(request,'About.html')

def Home(request):
    return render(request,'Home.html')



def register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        # form = MYFORM(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Created')
    context = { 'form' : form }
    return render(request,'appuser/reg.html',context)

def login_user(request):
    form = AuthenticationForm()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request , data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                passw = form.cleaned_data['password'] 
                print(name , passw , 'lkfajdfas')
                user =  authenticate(username=name,password=passw)
                if user is not None:
                    login(request,user)
                    print('klsdjrlef')
                    return redirect('Profile')
    else:
        return redirect('Profile')
    context = {'form':form}
    return render(request,'appuser/login.html',context)


def Profile(request):
    context = {}
    if request.user.is_authenticated:
        context['user'] = request.user
        return render(request,'appuser/Profile.html',context)
    else:
        return redirect('Login')

def Provider_page(request):
    providers = provide.objects.filter(who_provider=request.user,accepted=False)

    context = {
        'providers':providers
    }


    return render(request,'appuser/provider.html',context)

def discard_provider(request,pid):
    temp = provide.objects.get(id=pid)
    # temp.delete()
    return redirect('Profile')

def make_req(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    form = SeekerForm()
    if request.method == 'POST':
        form = SeekerForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.accepted = False
            form.who_seeker = request.user
            form.save()
            print('hwlo')
            return redirect('Profile')
    context = {'form':form}
    return render(request,'appuser/seekerform.html',context)

def accept_provider(request,pid):
    temp = provide.objects.get(id=pid)
    temp.accepted = True
    temp.save()
    return redirect('Profile')


def Seeker_page(request):
    return render(request,'appuser/seeker.html')


def log_out(request):
    logout(request)
    return redirect('Login')

def show_data(request,id):
    if request.user.is_authenticated:
        data = OWNUSER.objects.get(pk=id)
        form = AdminProfileForm(instance=data)
        context = {'form':form}
        return render(request,'appuser/user_data.html',context)
    else:
        return redirect('Login')

def change_pass(request):
    form = PasswordChangeForm(user=request.user)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                # update_session_auth_hash() THis function maintain the User profilr
                # If we dont use this then it will automatically log-out user 
                update_session_auth_hash(request,form.user)
                return redirect('Profile')            
    else:
        return redirect('Login')
    context={ 'form':form }
    return render (request,'appuser/changepass.html',context)

def change_pass1(request):
    #this one will not check  old password
    form = SetPasswordForm(user=request.user)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                # update_session_auth_hash() THis function maintain the User profilr
                # If we dont use this then it will automatically log-out user 
                update_session_auth_hash(request,form.user)
                return redirect('Profile')            
    else:
        return redirect('Login')
    context={ 'form':form }
    return render (request,'appuser/changepass1.html',context)


