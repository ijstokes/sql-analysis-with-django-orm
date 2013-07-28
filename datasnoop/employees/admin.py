from django.contrib import admin

# Register your models here.

from datasnoop.employees.models import Departments, DeptEmp, DeptManager, Employees, Salaries, Titles

for cls in (Departments, DeptEmp, DeptManager, Employees, Salaries, Titles):
    admin.site.register(cls)
