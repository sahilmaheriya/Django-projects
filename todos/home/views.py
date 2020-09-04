from django.shortcuts import render,redirect
from home.forms import StudentRegister
from home.models import Student
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = StudentRegister(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = StudentRegister()
        stu = Student.objects.all()
    return render(request, 'home.html',{'form':fm, 'student':stu})

def update(request, id):
    if request.method == "POST":
        pi = Student.objects.get(pk = id)
        fm = StudentRegister(request.POST, instance=pi)
        if fm.is_valid():
            messages.success(request, 'Your Data Will Be Updated')
            fm.save()
                        
    else: 
        pi = Student.objects.get(pk = id)
        fm = StudentRegister()
    return render(request, 'update.html',{'id':id, 'form':fm})

def delete_data(request,id):
    if request.method == 'POST':
        pi = Student.objects.get(pk= id)
        pi.delete()
        return redirect('/')

