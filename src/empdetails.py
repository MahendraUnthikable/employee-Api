import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import detailSerializer
from .models import employeeDetail
from django.shortcuts import  get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
    


class employeeData(APIView):
    """this class is used to create employee profile and also can
    update and delete data, all method are define below for 
    modifying employee details.
    """
    authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def post(self, request):
        """this function is used to save employee all details
        in the database.
        """
        serializer=detailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"sucess",
                             "data":serializer.data
                           }, 
                           status=status.HTTP_200_OK)
        else:
            return Response({"status":"error ", "data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)    
    
    def get(self,request,id=None):
        """tihs function is used to get employee details
        from the databse by their id and also get 
        complete data from database.
        """
        if id:
            item = employeeDetail.objects.get(id=id)
            serializer = detailSerializer(item)
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        
        item=employeeDetail.objects.all()
        serializer=detailSerializer(item, many=True)
        return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)

    def patch(self,request, id=None):
        """this function is used to modify employee
        data from the database and also can modify
        spacific employee details.
        """
        if id:
            item = employeeDetail.objects.get(id=id)
            serializer = detailSerializer(item, data=request.data, partial=True)
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
            item = employeeDetail.objects.get(id=id)
            serializer = detailSerializer(item,data=request.data)            
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
            item = get_object_or_404(employeeDetail,id=id)
            item.delete()
            return Response({"status":"success","data":"Item Deleted"})            