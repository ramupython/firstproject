from django import forms  
from .models import Employee_Data  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee_Data  
        fields = "__all__"  