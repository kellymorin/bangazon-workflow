from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Department, Training, Computer

def index(request):
    context = {}
    return render(request, 'agileHR/index.html', context)

def employee(request):
    employee_list = Employee.objects.all()
    context = {'employee_list': employee_list}
    return render(request, 'agileHR/employee.html', context)

def department(request):
    context = {}
    return render(request, 'agileHR/department.html', context)

def training(request):
    context = {}
    return render(request, 'agileHR/training.html', context)

def computer(request):
    context = {}
    return render(request, 'agileHR/computer.html', context)