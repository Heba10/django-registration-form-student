from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from sellingportal import models
from sellingportal import forms

def index(request):
	context={'name':'heba','b':'j','o':['u','l','p']}
	return render(request,'index.html',context)
    # return HttpResponse('Hello, welcome to the index page.')
	

def student(request):
	students=models.Student.objects.all()
	context={'students':students}
	return render(request,'student.html',context)
    # return HttpResponse('Hello, welcome to the student page.')

def degree(request,student_id):
    # return HttpResponse('this is degree of student id.'+ student_id)
    d=models.Degree.objects.filter(student_id=student_id)
    student=models.Student.objects.get(id=student_id)
    data=forms.DegreeRegistar(request.POST or None)
    msg=''
    if data.is_valid():
    	degree=models.Degree()
    	degree.student_degree=data.cleaned_data['student_degree']
    	degree.student_id=student
    	degree.save()
    	msg='data saved'
    context={'d':d,'data':data,'msg':msg}
    return render(request,'d.html',context)

def Registar(request):
	data=forms.Registar(request.POST or None)
	msg=''
	if data.is_valid():
		student=models.Student()
		student.first_name=data.cleaned_data['first_name']
		student.last_name=data.cleaned_data['first_name']
		student.age=data.cleaned_data['age']
		student.date_birth=data.cleaned_data['date_birth']
		student.save()
		msg='data saved'
	context={'data':data,'msg':msg}
	return render(request, 'Registar.html',context)
