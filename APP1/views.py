from django.shortcuts import redirect, render
from django.contrib import messages
import random
from django.contrib.auth.models import User,auth
import requests
import json
import time

   
   
# Create your views here.

def ref(phn):
    global t

    t=time.time()
    global ot  
    ot=str(random.randint(1000,9999))
    
    # mention url
    url = "https://www.fast2sms.com/dev/bulk"
    # create a dictionary 
    my_data = { 
        # Your default Sender ID 
        'sender_id': 'FSTSMS', 
        
        # Put your message here! 
        'message': ot, 
        
        'language': 'english', 
        'route': 'p', 
        
        # You can send sms to multiple numbers 
        # separated by comma. 
        'numbers':phn    
    } 

    # create a dictionary 
    headers = { 
        'authorization': 'KHJ1gZ5oXTBpGEAMSvCzhb4r39Dcta26QfmniWRxYjI7PLV8OwVjg43kpmeSMKT1fiqQ8rEXNohU0csG', 
        'Content-Type': "application/x-www-form-urlencoded", 
        'Cache-Control': "no-cache"
    }


    # make a post request 
    response = requests.request("POST",url,data = my_data,headers = headers) 

    returned_msg = json.loads(response.text) 

    # print the send message 
    print(returned_msg['message'])
   
    
def phn(request):
    return render(request,'phn.html')


def register(request):
   if request.method=='POST':
    global pn
    pn=request.POST['phn']
    ref(pn)
    return render(request,'otp.html')

    
   else:
       
       return render(request,'otp.html')

def otp(request):
      ref(pn)
      return render(request,'otp.html')
    


def verify(request):
      T=time.time()
      if (T-t)<=30:
            s=request.GET['tt']
            if s==ot:
                return redirect('APP2/login')
            else:
                h=0
                messages.info(request,' wrong otp')
                return redirect('register',)
      else:
           messages.info(request,'otp_time_out,')
           return redirect('register')