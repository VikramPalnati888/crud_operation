from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from student_app.models import *


def login(request):
    if request.method == "POST":
        print("ppppp")
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            user_name = request.user
            messages.success(request, 'Login Successful')
            return redirect('StudentDetails_Get')
        else:
            messages.error(request, 'Invalid Login Credentials')
            return redirect('login')
    else:
        user_name = request.user
        return render(request, 'login.html', {'user': user_name})


def Logout(request):
    logout(request)
    return redirect('login')


@login_required
def StudentDetailsPost(request):
    if request.method == "POST":
        try:
            student_obj_exist = StudentDetails.objects.get(Student_Name=request.POST['Student_Name'],
                                                           Subject=request.POST['Subject'])
            messages.error(request, "Student Details Already Exist")
        except:
            StudentDetails.objects.create(Student_Name=request.POST['Student_Name'],
                                          Subject=request.POST['Subject'], Marks=int(request.POST['Marks']))
            messages.success(request, "Student Marks Added Successful")
        return redirect('StudentDetails_Get')
    return render(request, 'student_form.html', {'message': "Student Marks Added Successful"})


@login_required
def StudentDetailsGet(request):
    if request.method == "GET":
        data = {}
        data_list = []
        StudentDetails_qs = StudentDetails.objects.all().order_by('-id')
        for dt in StudentDetails_qs:
            data[dt.id] = {
                "id": dt.id,
                "Student_Name": dt.Student_Name,
                "Subject": dt.Subject,
                "Marks": int(dt.Marks),
            }
        data_list.append(data)
        return render(request, 'student_form.html', {'response': data_list})


@login_required
def StudentDetailsEdit(request, pk):
    try:
        StudentDetails_data = StudentDetails.objects.get(id=pk)
        if request.method == 'POST':
            student_obj = StudentDetails.objects.get(id=pk)
            student_obj.Student_Name = request.POST['Student_Name']
            student_obj.Subject = request.POST['Subject']
            student_obj.Marks += int(request.POST['Marks'])
            student_obj.save()
            return redirect('StudentDetails_Get')
        return render(request, "student_form.html", {'data': StudentDetails_data})
    except Exception as e:
        messages.error(request, str(e))


@login_required
def Delete(request, id):
    student_obj = StudentDetails.objects.get(id=id)
    student_obj.delete()
    return redirect("StudentDetails_Get")