from django.shortcuts import render,redirect
from home.forms import StudentForm
from home.models import Student

# Create your views here.

def home(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = StudentForm()
        stu = Student.objects.all()
    return render(request, 'home.html',{'form':fm,'student':stu})

def delete_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk = id)
        pi.delete()
        return redirect('/')
    
def update_data(request, id):
    if request.method == 'POST':
        pi  = Student.objects.get(pk = id)
        fm = StudentForm(request.POST, instance= pi)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        pi  = Student.objects.get(pk = id)
        fm = StudentForm(instance= pi)
    return render(request, 'update.html',{'form':fm})


