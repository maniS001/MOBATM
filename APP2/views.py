from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.


def home(request):
    return render(request,'home.html')

def reg(request):
    c=0
    if request.method=='POST':
       
       name=request.POST['name']
       pass1=request.POST['pass1']
       pass2=request.POST['pass2']
       if pass1==pass2:
           if User.objects.filter(username=name).exists():
               c=1
               messages.info(request,'you are already having an account')
               return render (request,'register.html',{'c':c}) 
           else:
                user=User.objects.create_user(username=name,password=pass1)
                user.save
                return render(request,'login.html')
       else:
            c=2
            messages.info(request,'password not match')
            return render(request,'register.html',{'c':c})

    else:
        return render(request,'register.html',{'c':c})
def login(request):
  if request.method=='POST':
     name=request.POST['name']
     password=request.POST['pass']
     user=auth.authenticate(username=name,password=password)
     if user is not None:
         auth.login(request,user)
         return render(request,'home.html')
     else:
         messages.info(request,'wrong password or wrong username')
         return redirect('login')
        
  else:
     return render(request,'login.html')
    
