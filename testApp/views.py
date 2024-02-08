from django.shortcuts import render
from django.http import HttpResponseServerError
from testApp.models import Employee
from testApp.forms import EmployeeForm
# Create your views here.


def Employee_views(request):
    emp_list= Employee.objects.all()
    return render(request, 'testApp/index.html', {'emp_list': emp_list})

def EmpInsert_view(request):
    form= EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
    if form.is_valid():
        form.save()
          
    else:
        form = EmployeeForm()
    return render(request, 'testApp/insert.html', {'form': form})
   

