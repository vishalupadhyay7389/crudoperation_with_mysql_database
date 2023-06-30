from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import User
from crudapp.form import Userform
from http import HTTPStatus

# Create your views here.

def index(request):
    if request.method == "POST":
        form = Userform(request.POST)
        if form.is_valid:
            try:
                form.save()
                return HttpResponse("<h1>DATA SEND TO DATABASE</h1>")
            except:
                pass
    form = Userform()
    return render(request,'index.html',{'form':form})

def show(request):
    form = User.objects.all()
    context={
        'form':form
    }
    return render(request,'show.html',context)

def delete(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/show')

def edit(request,id):
    user = User.objects.get(id=id)
    # context = {
    #     'user':user
    # }
    return render(request,'edit.html',{'user':user})

def update(request,id):
    user = User.objects.get(id=id)
    form = Userform(request.POST,instance=user)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'user':user})
    
    
                
                
                
                
        
            
