from django.shortcuts import render, redirect
from employees.forms import EmployeeForm, EmployeeInputForm

# Create your views here.
def registration(request):
    if request.method == 'GET':
        form = EmployeeForm
        return render(request, 'registration.html', {'form':form})
    else:
        form = EmployeeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('registration')

def employees(request):
    if request.method == 'GET':
        form = EmployeeInputForm
        return render(request, 'employees.html', {'form':form})
    else:
        form = EmployeeInputForm(request.POST)
    if form.is_valid():
           form.save()
           return redirect('employees')






