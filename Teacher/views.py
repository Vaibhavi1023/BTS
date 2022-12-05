from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth

def home(request):
    return render(request ,'home.html')
def frontpage(request):
    if request.method == 'POST':
       username=request.POST['username']
       password=request.POST['password']
       x=auth.authenticate(username=username,password=password)
       if x is None:
             return redirect('/')
             print(hi)
       else:
            return render(request,'registeration.html')
            print(hello)
    else:
        return render(request,'attendance.html')
        print(hii)
# Create your views here.
