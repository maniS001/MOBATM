

from django.urls import path
from .import views
urlpatterns = [ 
    
    path('',views.phn, name='home'),
    path('register',views.register,name='register'),
    path('otp',views.otp,name='otp'),
    path('verify',views.verify,name='verify')
    
] 