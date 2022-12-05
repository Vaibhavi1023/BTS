from django.http import HttpResponse
from django.shortcuts import render


def aboutus(request):
    return HttpResponse("<b>welcome to this page<b>")
def student(request):
    return HttpResponse("hello student")
    

    
   
       
   

def registeration(request):
    return render(request,"registeration.html")

def registaration_data(req):
    data =  body.data
    print(data)
    return HttpResponse('<h1>data found</h1>')
