import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *


def index(request):
    context = {}
    return render(request, "agileHR/index.html", context)

def employee(request):
    """This method queries the database for all employees ordered by last name and renders the employee page

    Author: Rachel Daniel

    Returns:
        render -- loads the employee.html template.
    """
    employee_list = Employee.objects.order_by('last_name')
    context = {'employee_list': employee_list}
    return render(request, 'agileHR/employee.html', context)

def employee_detail(request, employee_id):
    """This method queries the database for the employee clicked on employee page as well as their current (non-revoked) computer, and renders the employee detail page

    Author: Rachel Daniel

    Returns:
        render -- loads the employee_detail.html template.
    """
    employee = get_object_or_404(Employee, pk=employee_id)
    employee_computer = EmployeeComputer.objects.filter(employee_id=employee_id).filter(date_revoked=None)
    context = {"employee": employee, "employee_computer": employee_computer}
    return render(request, "agileHR/employee_detail.html", context)


def employee_add(request):
    """This method queries the database for the departments and renders the form for adding a new employee. Upon submit, the method collects form data from post request, validates, and adds a new employee

    Author: Rachel Daniel

    Returns:
        render -- loads the employee_form.html template when originally navigating to the page, or renders form with error message if submit was unsuccessful
        HttpResponseRedirect -- loads the employee page if add was successful
    """
    departments = Department.objects.order_by('name')

    if request.method == "POST":
        try:
            department = get_object_or_404(Department, pk=request.POST["department"])
            first_name = (request.POST["first_name"])
            last_name = (request.POST["last_name"])
            start_date = (request.POST["start_date"])
            is_supervisor = request.POST.get("is_supervisor", "") == "on"
            if first_name == "" or last_name == "" or start_date == "":
                return render(request, "agileHR/employee_form.html", {"error_message": "You must complete all fields in the form.", "departments": departments,
                "first_name": first_name,
                "last_name": last_name,
                "start_date": start_date,
                "department": department
                })
            else:
                new_employee = Employee(first_name=first_name, last_name=last_name, department=department, is_supervisor=is_supervisor, start_date=start_date)
                new_employee.save()
                messages.success(request, 'Saved!')
                return HttpResponseRedirect(reverse("agileHR:employee"))


        except KeyError:
            return render(request, 'agileHR/employee_form.html', {
            'error_message': "You must complete all fields in the form.", "departments": departments
            })
    else:
        context = {"departments": departments}
        return render(request, "agileHR/employee_form.html", context)

def department(request):
    """This method queries the database for department and related employee information and renders the department template.

    Author: Brendan McCray

    Returns:
        render -- loads the department.html template.
    """

    departments = Department.objects.all()
    employees = Employee.objects.all()
    dept_size = Employee.objects.raw("""SELECT COUNT(agileHR_employee.department_id) AS "count", agileHR_department.id
        FROM agileHR_employee
        JOIN agileHR_department WHERE agileHR_department.id = agileHR_employee.department_id
        GROUP BY department_id"""
    )

    context = {
        "departments": departments,
        "employees": employees,
        "dept_size": dept_size
    }
    return render(request, "agileHR/department.html", context)

def department_detail(request, dept_id):
    """This method queries the database for a specific department and its employee information and renders the department_detail template.

    Author: Brendan McCray

    Returns:
        render -- loads the department_detail.html template.
    """

    department = get_object_or_404(Department, pk=dept_id)
    try:
        employees = Employee.objects.filter(department_id=dept_id)
        context = {"department": department, "employees": employees}
    except Employee.DoesNotExist:
        context = {"department": department}
    return render(request, 'agileHR/department_detail.html', context)

def departmentadd(request):
    if request.method == "POST":
        try:
          name = request.POST["dept_name"]
          budget = request.POST["dept_budget"]
          if name == "" or budget == "":
            return render(request, "agileHR/department_form.html", {
              "error_message": "You must complete all fields in the form.",
              "name": name,
              "budget": budget
              })
          else:
            new_dept = Department(name=name, budget=budget)
            new_dept.save()
            return HttpResponseRedirect(reverse("agileHR:department"))
        except KeyError:
          return render(request, "agileHR/department_form.html", {
            "error_message": "You must complete all fields in the form."
            })
    # if navigating through this method, only the form is loaded (no post in request)
    else:
      context = {}
      return render(request, 'agileHR/department_form.html', context)

def training(request):
    """Displays the list of upcoming training sessions with links to details for each one.

    Author: Kelly Morin

    Returns:
        render -- Returns the training template
    """

    training_list = Training.objects.filter(start_date__date__gte=datetime.date.today()).order_by('start_date')
    context = {'training_list': training_list}
    return render(request, "agileHR/training.html", context)


def training_detail(request, training_id):
    """Displays the details about a single training session hosted by the company

    Author: Kelly Morin

    Arguments:
        training_id {int} -- The pk of the training seession being requested

    Returns:
        render -- Returns the training_detail template
    """

    training_details = get_object_or_404(Training, pk=training_id)
    attendee_size = len(EmployeeTraining.objects.filter(training_id=training_id))
    context = {'training_details': training_details, 'attendee_size': attendee_size}
    return render(request, 'agileHR/training_detail.html', context)

def training_edit(request):
    context={}
    return render(request, 'agileHR/training_form.html', context)

def training_add(request):
    """Displays form to add a new training session

    Author: Kelly Morin

    Returns:
        render -- returns the training form template, an error message to be displayed or the training template with the new training session added
    """

    if request.method == 'POST':
        try:
            title= request.POST['training_title']
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
            max_attendees = request.POST['max_attendees']
            if title == '' or start_date == '' or end_date == '' or max_attendees == '':
                return render(request, 'agileHR/training_form.html', {'error_message': "You must complete all fields in the form"})
            else:
                new_training = Training(title=title, start_date=start_date, end_date=end_date, max_attendees=max_attendees)
                new_training.save()
                return HttpResponseRedirect(reverse('agileHR:training'))
        except KeyError:
            return render(request, 'agileHR/training_form.html', {'error_message': "You must complete all fields in the form"})
    else:
        context={}
        return render(request, 'agileHR/training_form.html', context)


def computers(request):
    """Displays the list of computers currently owned by the company with links to details for each one.

    Author: Sebastian Civarolo

    Returns:
        render -- loads the computer.html template.
    """

    computers = Computer.objects.all()
    context = {
        "computers": computers
    }
    return render(request, 'agileHR/computers.html', context)


def computer_detail(request, computer_id):
    """Displays the details about a single computer owned by the company.

    Arguments:
        computer_id {int} -- The pk of the computer being requested.

    Returns:
        render -- Returns the computer_detail template
    """

    computer = get_object_or_404(Computer, pk=computer_id)

    context = {
        "computer": computer
    }

    return render(request, "agileHR/computer_detail.html", context)


def new_computer(request):
    """Displays the form to add a new computer, and checks for all inputs before saving to the database.

    Author: Sebastian Civarolo

    Returns:
        render -- Returns the form with an error message, or if successful, returns the new detail page.
    """

    if request.method == "POST":

        try:
            make = request.POST["make"]
            model = request.POST["model"]
            serial_no = request.POST["serial_no"]
            purchase_date = request.POST["purchase_date"]

            if make is "" or model is "" or serial_no is "" or purchase_date is "":
                return render(request, "agileHR/computer_new.html", {
                    "error_message": "Please fill out all fields",
                    "make": make,
                    "model": model,
                    "serial_no": serial_no,
                    "purchase_date": purchase_date
                })
            else:
                new_computer = Computer(make=make, model=model, serial_no=serial_no, purchase_date=purchase_date)
                new_computer.save()
                return HttpResponseRedirect(reverse("agileHR:computer_detail", args=(new_computer.id,)))
        except KeyError:
            return render(request, "agileHR/computer_new.html", {
                "error_message": "Please fill out all fields"
            })
    else:
        context = {}
        return render(request, "agileHR/computer_new.html", context)


def delete_computer(request, computer_id):
    """Deletes a computer ONLY if it has NEVER been assigned to an employee.

        Arguments:
            computer_id {int} -- the ID of the computer to be deleted.

        Author: Sebastian Civarolo
    """

    if request.method == "POST":
        computer = Computer.objects.get(pk=computer_id)
        computer.delete()
        return HttpResponseRedirect(reverse("agileHR:computers"))

    else:
        computer = Computer.objects.get(pk=computer_id)
        assignments = EmployeeComputer.objects.filter(computer_id=computer_id)

        if len(assignments) == 0:
            context = {
                "computer": computer,
                "can_delete": True
            }
        else :
            context = {
                "computer": computer,
                "can_delete": False
            }
        return render(request, "agileHR/computer_delete.html", context)