from django.urls import path
from . import views

app_name = "agileHR"
urlpatterns = [
    path("", views.index, name="index"),
    path("employees/", views.employee, name="employee"),
    path("employees/<int:employee_id>/", views.employee_detail, name="employee_detail"),
    path("employees/new", views.employee_form, name="employee_form"),
    path("employees/add", views.employee_add, name="employee_add"),
    path("departments/", views.department, name="department"),
    path("departments/<int:dept_id>/", views.department_detail, name="department_detail"),
    path("trainings/", views.training, name="training"),
    # ex: /bangazon/trainings/5
    path("trainings/<int:training_id>", views.traindetail, name="traindetail"),
    # ex: /bangazon/computers/
    path("computers/", views.computer, name="computer"),
    # ex: /bangazon/computers/12
    path("computers/<int:computer_id>", views.computer_detail, name="computer_detail")
]

