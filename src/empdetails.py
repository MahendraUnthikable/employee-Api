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
    authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def post(self, request):
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
        if id:
            item = employeeDetail.objects.get(id=id)
            serializer = detailSerializer(item)
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        
        item=employeeDetail.objects.all()
        serializer=detailSerializer(item, many=True)
        return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)

    def patch(self,request, id=None):
        if id:
            item = employeeDetail.objects.get(id=id)
            serializer = detailSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
               serializer.save()
               return Response({"status":"sucess","data":serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"error ", "data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,id=None):
        if id:
            item = employeeDetail.objects.get(id=id)
            serializer = detailSerializer(item,data=request.data)            
            if serializer.is_valid():
               serializer.save()
               return Response({"status":"sucess","data":serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"error ", "data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id=None):            
        if id:
            item = get_object_or_404(employeeDetail,id=id)
            item.delete()
            return Response({"status":"success","data":"Item Deleted"})            