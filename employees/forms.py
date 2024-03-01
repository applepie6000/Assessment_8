from django import forms
from employees.models import Register, Employee


class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Register
        fields = ('first_name', 'last_name', 'phone_no', 'password')


class EmployeeInputForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'employee', 'ID_no', 'phone_no')

