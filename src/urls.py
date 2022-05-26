from django.urls import path
from .views import employeeProfile,register
from .empdetails import employeeData
from .auth import employeeLogin

urlpatterns =[
    path('employeeprofile/', employeeProfile.as_view()),
    path('employeeprofile/<int:id>', employeeProfile.as_view()),
    path('employeeregistration/',register.as_view()),
    path('employeelogin/', employeeLogin.as_view()),
    path('employeedetails/',employeeData.as_view())

]