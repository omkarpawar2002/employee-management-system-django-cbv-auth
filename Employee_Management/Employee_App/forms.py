from django import forms
from .models import Employee

gender_choices = [
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER')
]

dept_choices = [
    ('IT','IT'),
    ('ADMIN','ADMIN'),
    ('SALES','SALES'),
    ('OPERATION','OPERATION'),
    ('HR','HR')
]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'emp_id':forms.NumberInput(attrs={
                'placeholder':'E.g.,101'
            }),
            'first_name':forms.TextInput(attrs={
                'placeholder':'Enter First Name'
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Enter Last Name'
            }),
            'gender':forms.RadioSelect(choices=gender_choices),
            'phone_no':forms.TextInput(attrs={
                'placeholder':'+91 ***** *****'
            }),
            'city':forms.TextInput(attrs={
                'placeholder':'Enter City Name'
            }),
            'address':forms.Textarea(attrs={
                'rows':'3',
                'placeholder':'Enter your address here .....'
            }),
            'dept':forms.Select(choices=dept_choices),
            'email':forms.EmailInput(attrs={
                'placeholder':'youremail@gmail.com'
            }),
            'password':forms.PasswordInput(attrs={
                'type':'password'
            })
        }