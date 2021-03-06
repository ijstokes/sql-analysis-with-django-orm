from django.contrib import admin

# Register your models here.

from datasnoop.employees.models import Departments, DeptEmp, DeptManager, Employees, Salaries, Titles

#for cls in (Departments, DeptEmp, DeptManager, Employees, Salaries, Titles):
#    admin.site.register(cls)

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('dept_name', 'dept_no')
    search_fields = ['dept_name']
admin.site.register(Departments, DepartmentsAdmin)

class DeptEmpAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'dept_no', 'from_date', 'to_date')
    list_filter  = ('dept_no', 'from_date', 'to_date')
    search_fields = ['emp_no__last_name', 'dept_no__dept_name']
    date_hierarchy = 'from_date'
admin.site.register(DeptEmp, DeptEmpAdmin)

class DeptManagerAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'dept_no', 'from_date', 'to_date')
    list_filter  = ('dept_no', 'from_date', 'to_date')
    search_fields = ['emp_no__last_name', 'dept_no__dept_name']
    date_hierarchy = 'from_date'
admin.site.register(DeptManager, DeptManagerAdmin)

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'last_name', 'first_name', 'gender', 'birth_date', 'hire_date')
    list_filter  = ('gender', 'birth_date', 'hire_date')
    search_fields = ['emp_no__last_name']
    date_hierarchy = 'birth_date'
admin.site.register(Employees, EmployeesAdmin)

class SalariesAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'salary', 'from_date', 'to_date')
    list_filter  = ('from_date', 'to_date')
    search_fields = ['emp_no__last_name']
    date_hierarchy = 'from_date'
admin.site.register(Salaries, SalariesAdmin)

class TitlesAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'title', 'from_date', 'to_date')
    search_fields = ['emp_no__last_name']
    date_hierarchy = 'from_date'
admin.site.register(Titles, TitlesAdmin)
