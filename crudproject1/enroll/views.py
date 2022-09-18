import email
from unicodedata import name
from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student

# Create your views here.



# this function will add new item and show all iteams

def add_show(request):

    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        print('fim = ', fm)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            check_email = Student.objects.filter(email=em)
            print('ccheek email = ', check_email)

            pw = fm.cleaned_data['password']
            if len(check_email) == 0:
                reg = Student(name=nm, email=em, password = pw )
                fm.save()
                fm = StudentRegistration()
            else:
                stud = Student.objects.all()
                msg = 'Please try to  another email '
                return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud, "msg": msg})
            return HttpResponseRedirect('/')
    else:
        fm = StudentRegistration()
    stud = Student.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


# This function will update and edit
def update_data(request, id):
    pi = Student.objects.get(pk = id)
    fm = StudentRegistration(instance=pi)
    if request.method == 'POST':
        pi = Student.objects.get(pk = id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid:
            fm.save()
            return HttpResponseRedirect('/')
        else:
            pi = Student.objects.get(pk = id)
            fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': fm})


# this function will delete data
def delete_data(request, id):
   
    if request.method == 'POST':
        
        pi = Student.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')
    return render(request, "delete_view.html",)