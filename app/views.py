from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

from .models import Records
# Create your views here.

# function-->
def home(request):
    return render(request,"home.html")

def authenticatePage(request):
    mydict = {
        'error':False
    }
    if request.user.is_authenticated:
       return redirect('/home2')
    else: 
        if request.method == 'POST':
            username=request.POST.get('signup_username')
            email=request.POST.get('signup_email')
            password=request.POST.get('signup_password')
            # print(username,email,password)
            if username is not None:
                try:
                    new_user = User.objects.create_user(username=username,email=email,password=password)
                    new_user.save()
                    login(request,new_user)
                except:
                    mydict = {'error':True}
                    return render(request,'authentication.html',context=mydict)
                return render(request,'home2.html')
        if request.method == 'POST':
            Lusername = request.POST.get('login_username')
            Lpass = request.POST.get('login_password')
            user = authenticate(username=Lusername,password=Lpass)
            # print(Lusername,Lpass)
            # print(user)
            if user is not None:
                login(request,user)
                return redirect('/home2')
            else:
                return render(request,'authentication.html')
            
        return render(request,'authentication.html')
def home2(request):
    if request.user.is_authenticated:
        student_objs = Records.objects.all()
        print(student_objs)
    return render(request, 'home2.html',{'student_objs':student_objs})  

def saveData(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        num = request.POST.get('number')
        city = request.POST.get('city')
        roll = request.POST.get('roll')
        attendance = request.POST.get('attendance')
        print(n,num,city,roll,attendance)
        if attendance == 'absent':
            student = Records(name=n,number=num,city=city,roll=roll)
        else:
            student = Records(name=n,number=num,city=city,roll=roll,attendance=True)
        student.save()  

    return redirect('/home2')  

def signout(request):
    logout(request)
    return redirect('/')

def delete(request,id):
    student = Records.objects.get(id=id)
    student.delete()
    return redirect('/home2')