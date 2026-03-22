from django.urls import path
from .views import ( AddEmployee , ShowEmployee , UpdateEmployee , DeleteEmployee )

urlpatterns = [
    path('',AddEmployee.as_view(),name='AddEmployee'),
    path('add_emp/',AddEmployee.as_view(),name='AddEmployee'),
    path('show_emp/',ShowEmployee.as_view(),name='ShowEmployee'),
    path('update_emp/<int:pk>/',UpdateEmployee.as_view(),name='UpdateEmployee'),
    path('delete_emp/<int:pk>/',DeleteEmployee.as_view(),name='DeleteEmployee'),
]