from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from .models import *
from django.db.models import Q


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
        providers = seek.objects.filter(who_provider=request.user,status=0)
        context['user'] = request.user
        context['providers'] = providers
        return render(request,'appuser/Profile.html',context)
    else:
        return redirect('Login')

def search(request):
    context={}
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print('here')
            pcity = form.cleaned_data['pcity']
            print("pcity",len(pcity))
            dcity = form.cleaned_data['dcity']
            weight = form.cleaned_data['weight']

            try:
                pc = City.objects.filter(city_name=pcity)[0]
            except:
                pc=request.user.city
            try:
                dc = City.objects.filter(city_name=dcity)[0]
            except:
                dc = request.user.city

            print("safsf" , pc ,dc )

            data1 = provide.objects.all()

            data = data1.filter( (Q(p_pickup_city = pc) | Q(p_dest_city = dc) )  | Q(remaining_weight__lte = weight))
            # data = provide.objects.filter(p_pickup_city = form.cleaned_data['dcity'])
            print(data)
            context['data'] =data
            
    context['form']=form
    return render(request,'appuser/search.html',context)

def Provider_page(request):

    if not request.user.is_authenticated:
        return redirect('Login')
    
    form = ProviderForm()
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            ft = form.save(commit=False)
            return redirect('Provider')
    # providers = provide.objects.filter(who_provider=request.user,accepted=False)
    # providers = seek.objects.filter(who_provider=request.user,status=0)

    context = {
        # 'providers':providers,
        'form':form
    }


    return render(request,'appuser/provider.html',context)

def discard_provider(request,pid):
    temp = seek.objects.get(id=pid)
    # temp.delete()
    return redirect('Profile')

def make_req(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    form = SeekerForm(request.POST or None)
    if request.method == 'POST':
        form = SeekerForm(request.POST)
        if form.is_valid():
            ft = form.save(commit=False)
            ft.who_seeker = request.user
            ft.status = 0
            ft.save()
            return redirect('Profile')
    context = {'form':form}
    return render(request,'appuser/seekerform.html',context)

def accept_provider(request,pid):
    temp = seek.objects.get(id=pid)
    temp.status = 1
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


