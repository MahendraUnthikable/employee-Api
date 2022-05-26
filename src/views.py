import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import registratoinSerializer
from .models import employeeRegistratoin
from django.shortcuts import  get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


logger = logging.getLogger(__file__)

class register(APIView):
    """this class is used to register employee data 
    and save employee all details
    in the database. 
    """
    def post(self, request):
        serializer=registratoinSerializer(data=request.data)
        useremail=request.data['email']
        userphone=request.data['phone']
        
        if employeeRegistratoin.objects.filter(email=useremail).first():
            return Response({"status":"email already exists!!"})
        elif employeeRegistratoin.objects.filter(phone=userphone).first():
             return Response({"status":"phone number already exists!!"})  
        if serializer.is_valid():
            serializer.save()
            user=employeeRegistratoin.objects.filter(email=useremail).first()
            refresh = RefreshToken.for_user(user)
            return Response({"status":"sucess",
                             "data":serializer.data,
                             'Refresh_Token':str(refresh),
                             'Access_Token':str(refresh.access_token)
                           }, 
                           status=status.HTTP_200_OK)
        else:
            return Response({"status":"error ", "data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)    



class employeeProfile(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request,id=None):
        """tihs function is used to get employee details
        from the databse by their id and also get 
        complete data from database.
        """
        if id:
            item = employeeRegistratoin.objects.get(id=id)
            serializer = registratoinSerializer(item)
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        
        item=employeeRegistratoin.objects.all()
        serializer=registratoinSerializer(item, many=True)
        return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)

    def patch(self,request, id=None):
        """this function is used to modify employee
        data from the database and also can modify
        spacific employee details.
        """
        if id:
            item = employeeRegistratoin.objects.get(id=id)
            serializer = registratoinSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
               serializer.save()
               return Response({"status":"sucess","data":serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"error ", "data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,id=None):
        """this function can replace complete data 
        of the employee data from the database.
        """
        if id:
            item = employeeRegistratoin.objects.get(id=id)
            serializer = registratoinSerializer(item,data=request.data)            
            if serializer.is_valid():
               serializer.save()
               return Response({"status":"sucess","data":serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"error ", "data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id=None):            
        """this function is used to delete
        spacific employee details from the database.
        """
        if id:
            item = get_object_or_404(employeeRegistratoin,id=id)
            item.delete()
            return Response({"status":"success","data":"Item Deleted"})


