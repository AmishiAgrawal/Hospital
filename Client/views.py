from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from . models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        profile = request.FILES.get('profile')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        print('------------000000')

        print(profile)
        if password == cpassword:
            myuser = User.objects.create_user(role=role,first_name=fname,last_name=lname,username=username,password=password,profile_img=profile,address=address,state=state,city=city,zipcode=pincode)
            myuser.save()
            user = authenticate(request,username=username, password=password)
            print('------------')
            print(user.profile_img)
            if user is not None:
                login(request, user)
                messages.success(request, 'Account Created Successfully.')
                return dashboard(request)
            else:
                messages.error(request, 'No user found.')
                return redirect('/')
        else:
            messages.error(request, 'Passwords doesnot match')
            return redirect('/')
            
    
    else: 
        return render(request,'index.html')
    
def dashboard(request):
    user = request.user
    if user.role =='Patient':
        return render(request,'patient.html')
    else:
        return render(request,'doctor.html')
    
def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        authenticated_user = authenticate(request,username=username, password=password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            messages.success(request, 'Logged In Successfully!')
            return dashboard(request)
        else:
            messages.error(request, 'Incorrect Credentials.')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    
def user_logout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out.')
    return redirect('/')