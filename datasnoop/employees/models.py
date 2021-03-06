# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Departments(models.Model):
    #rowid       = models.IntegerField(primary_key=True)
    dept_idx    = models.IntegerField(primary_key=True)
    dept_no     = models.CharField(unique=True, max_length=4)
    dept_name   = models.CharField(unique=True, max_length=40)

    def __unicode__(self):
        return self.dept_name

    class Meta:
        db_table = 'departments'

class Employees(models.Model):
    emp_no      = models.IntegerField(primary_key=True)
    birth_date  = models.DateField()
    first_name  = models.CharField(max_length=14)
    last_name   = models.CharField(max_length=16)
    gender      = models.CharField(max_length=1)
    hire_date   = models.DateField()

    def __unicode__(self):
        return "%s, %s - %d" % (self.last_name, self.first_name, self.emp_no)

    class Meta:
        db_table = 'employees'

class DeptEmp(models.Model):
    #rowid       = models.IntegerField(primary_key=True)
    deptemp_idx = models.IntegerField(primary_key=True)
    emp_no      = models.ForeignKey(Employees, db_column='emp_no')
    dept_idx     = models.ForeignKey(Departments, db_column='dept_idx')
    from_date   = models.DateField()
    to_date     = models.DateField()

    def __unicode__(self):
        return "%s/%s (%s,%s)" % (self.dept_idx, self.emp_no, self.from_date, self.to_date)
        #return "%s/%s, %s" % (self.dept_no.dept_name, self.emp_no.last_name, self.emp_no.first_name)

    class Meta:
        db_table = 'dept_emp'

class DeptManager(models.Model):
    #rowid       = models.IntegerField(primary_key=True)
    manager_idx = models.IntegerField(primary_key=True)
    dept_idx    = models.ForeignKey(Departments, db_column='dept_idx')
    emp_no      = models.ForeignKey(Employees, db_column='emp_no')
    from_date   = models.DateField()
    to_date     = models.DateField()

    def __unicode__(self):
        return "%s/%s (Manager)" % (self.dept_idx, self.emp_no)

    class Meta:
        db_table = 'dept_manager'

class Salaries(models.Model):
    #rowid       = models.IntegerField(primary_key=True)
    salary_idx  = models.IntegerField(primary_key=True)
    emp_no      = models.ForeignKey(Employees, db_column='emp_no')
    salary      = models.IntegerField()
    from_date   = models.DateField()
    to_date     = models.DateField()

    def __unicode__(self):
        return "%d/%s" % (self.salary, self.emp_no)

    class Meta:
        db_table = 'salaries'

class Titles(models.Model):
    #rowid       = models.IntegerField(primary_key=True)
    titles_idx  = models.IntegerField(primary_key=True)
    emp_no      = models.ForeignKey(Employees, db_column='emp_no')
    title       = models.CharField(max_length=50)
    from_date   = models.DateField()
    to_date     = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return "%s/%s" % (self.title, self.emp_no)

    class Meta:
        db_table = 'titles'
