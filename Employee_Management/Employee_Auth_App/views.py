from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# User Registration (Sign Up)
class SignUp(View):
    def get(self,request):
        # Display empty user registration form
        form = UserCreationForm()
        template_name = 'Employee_Auth_App/sign_up.html'
        context = {'form':form}
        return render(request,template_name,context)
    
    def post(self,request):
        # Handle form submission for new user registration
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()  # Save new user to database
            return redirect('SignIn')  # Redirect to Sign In page
        else:
            return HttpResponse("Something Wrong While Registering User....")
        
# User Login (Sign In)
class SignIn(View):
    def get(self,request):
        # Display login form
        template_name = 'Employee_Auth_App/sign_in.html'
        context = {}
        return render(request,template_name,context)
    
    def post(self,request):
        # Handle login form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)  # Verify credentials
        if(user is not None):
            login(request,user)  # Log user
            return redirect('ShowEmployee')  # Redirect to employee list page
        else:
            return HttpResponse("Something Wrong While Sign In User...")
        
# User Logout (Sign Out)
class SignOut(View):
    def get(self,request):
        # Log out current user and redirect to Sign In page
        logout(request)
        return redirect('SignIn')
