from django import forms
from django.contrib import admin


# Register your models here.
from .models import Employee_Data,Departments,Dept_Manager,Dept_emp,Titles,Salaries

class Employee_DataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Employee_DataForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.emp_no:
            self.fields['emp_no'].widget.attrs['readonly'] = True
    class Meta:
        model=Employee_Data
        fields = ('emp_no', 'first_name','last_name','birth_date','gender','hire_date')

class Employee_DataAdmin(admin.ModelAdmin):
    fields = ('emp_no','first_name','last_name','birth_date','gender','hire_date')
    list_display = ['emp_no','first_name','last_name','birth_date','gender','hire_date']
    search_fields = ['first_name','last_name']
    list_filter = ('gender', 'last_name')
    #list_editable = ( 'first_name', 'last_name')
    form = Employee_DataForm
    list_per_page=20

class DepartmentsAdmin(admin.ModelAdmin):
    fields = ['dept_no', 'dept_name']
    list_display = ['dept_no', 'dept_name']
    search_fields = ['dept_name']

admin.site.register(Employee_Data,Employee_DataAdmin)
#admin.site.register(Employee_Data)
admin.site.register(Departments,DepartmentsAdmin)
admin.site.register(Dept_Manager)
admin.site.register(Dept_emp)
admin.site.register(Titles)
admin.site.register(Salaries)