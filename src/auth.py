from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import registratoinSerializer
from .models import employeeRegistratoin


class employeeLogin(APIView):
    """this class is used to authenticate employee 
      credentials from the database and authrize employee data. 
      """  
    def post(self,request):
        serializer = registratoinSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data['email']
            password = request.data['password']

            if not email:
              return 'Missing email', 400
            if not password:
              return 'Missing password', 400  
            
            useremail=employeeRegistratoin.objects.filter(email=email).first()
            userpass=employeeRegistratoin.objects.filter(password=password).first()
            if useremail and userpass is not None:
                return Response({"status":"Login sucessfully","data":serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Login Error","msg":"Access denied: wrong username or password."})

        
