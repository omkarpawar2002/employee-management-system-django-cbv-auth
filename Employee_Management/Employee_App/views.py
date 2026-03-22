from django.shortcuts import render,redirect,get_object_or_404
from .forms import EmployeeForm
from .models import Employee
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Add Employee
class AddEmployee(LoginRequiredMixin,View):
    login_url = 'SignIn'

    def get(self,request):
        # Display empty form for adding a new employee
        form = EmployeeForm()
        template_name = 'Employee_App/add_employee.html'
        context = {'form':form}
        return render(request,template_name,context)
    
    def post(self,request):
        # Handle form submission for new employee
        form = EmployeeForm(request.POST)
        if(form.is_valid()):
            form.save() # Save new employee record to DB
            return redirect('ShowEmployee') # Redirect to Show Employee List view
        else:
            return HttpResponse("Something Wrong While Adding Details...")
    
# Show Employee
class ShowEmployee(LoginRequiredMixin,View):
    login_url = 'SignIn'
    
    def get(self,request):
        # Fetch all employee records from DB
        objs = Employee.objects.all()
        template_name = 'Employee_App/show_employee.html'
        context = {'records':objs}
        return render(request,template_name,context)
    
# Update Employee
class UpdateEmployee(View):
    # Utility method to fetch employee by primary key (id)
    def get_object(self,pk):
        obj = get_object_or_404(Employee,id=pk)
        return obj

    def get(self,request,pk):
        # Display form pre-filled with employee data
        obj = self.get_object(pk)
        form = EmployeeForm(instance=obj)
        template_name = 'Employee_App/update_employee.html'
        context = {'form':form}
        return render(request,template_name,context)

    def post(self,request,pk):
        # Handle form submission for updating employee
        obj = self.get_object(pk)
        form = EmployeeForm(request.POST,instance=obj)
        if(form.is_valid()):
            form.save() # Save updated employee record
            return redirect('ShowEmployee')
        else:
            return HttpResponse("Something Wrong Happend While Updating Details....")

# Delete Employee
class DeleteEmployee(View):
    # Utility method to fetch employee by primary key (id)
    def get_object(self,pk):
        obj = get_object_or_404(Employee,id=pk)
        return obj

    def get(self,request,pk):
        # Display confirmation page before deletion
        obj = self.get_object(pk)
        template_name = 'Employee_App/delete_employee.html'
        context = {'obj':obj}
        return render(request,template_name,context)
    
    def post(self,request,pk):
        # Handle deletion after confirmation
        obj = self.get_object(pk)
        obj.delete() # Remove employee record from DB
        return redirect('ShowEmployee')