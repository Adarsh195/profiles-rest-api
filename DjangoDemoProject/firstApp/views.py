from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee
# Create your views here.
def employeeView(request):
    # emp_dict = {
    #     'emp_name':'Yash Singham',
    #     'emp_age':25,
    #     'emp_salary':50000,
    #     'emp_city':'Mumbai'
    #     }
    data = Employee.objects.all()
    emp_dict = {
        'emp':list(data.values())
    }
    return JsonResponse(emp_dict)
    
