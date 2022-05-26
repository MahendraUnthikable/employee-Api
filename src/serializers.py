from rest_framework import serializers
from .models import employeeRegistratoin, employeeDetail

class registratoinSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(required=False,max_length=100)
    last_name=serializers.CharField(required=False,max_length=100)
    email=serializers.CharField(required=True,max_length=100)
    password=serializers.CharField(required=True,max_length=100)
    phone=serializers.CharField(required=False,max_length=100)

    class Meta:
        model = employeeRegistratoin
        fields = ('__all__')
            
class detailSerializer(serializers.ModelSerializer):            
    employeeName=serializers.CharField(required=True,max_length=100)
    employeeDob=serializers.DateField(required=True)
    employeeEmail=serializers.EmailField(required=True,max_length=100)
    employeePhone=serializers.CharField(required=True,max_length=100)
    employeeCode=serializers.CharField(required=True,max_length=100)
    employeeAddress=serializers.CharField(required=True,max_length=500)

    class Meta:
        model = employeeDetail
        fields = ('__all__')