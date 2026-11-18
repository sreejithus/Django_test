from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from Employee.serializers import EmployeeSerializer
from Employee.models import Employee
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from Employee.permissions import Isowner

class Create_or_List(APIView):
            permission_classes = [Isowner]
            authentication_classes =[TokenAuthentication]
            def get(self,request):
                         qs = Employee.objects.all()
                         serializer_instance =  EmployeeSerializer(qs,many=True)
                         return Response(serializer_instance.data,status=status.HTTP_200_OK)
            def post(self,request):
                           serializer_instance = EmployeeSerializer(data=request.data)
                           if serializer_instance.is_valid():
                                      serializer_instance.save()
                                      return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
                           else:
                                    return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class RetrieveUpdateDelete(APIView):
                  permission_classes = [Isowner]
                  authentication_classes =[TokenAuthentication]
                  def get(self,request,id):
                                  obj  = get_object_or_404(Employee,id=id)
                                  self.check_object_permissions(obj)
                                  serializer_instace = EmployeeSerializer(obj)
                                  return Response(serializer_instace.data,status=status.HTTP_200_OK)
                  def put(self,request,id):
                                  
                                  obj  = get_object_or_404(Employee,id=id)
                                  self.check_object_permissions(request,obj)
                                  serializer_instace = EmployeeSerializer(obj,data =request.data)
                                  if serializer_instace.is_valid():
                                              serializer_instace.save()
                                              return Response(serializer_instace.data,status=status.HTTP_200_OK)
                                  else:
                                          return Response(serializer_instace.errors,status=status.HTTP_400_BAD_REQUEST)
                  def patch(self,request,id):
                                                      
                                                      obj  = get_object_or_404(Employee,id=id)
                                                      self.check_object_permissions(request,obj)
                                                      serializer_instace = EmployeeSerializer(obj,data =request.data,partial=True)
                                                      if serializer_instace.is_valid():
                                                                  serializer_instace.save()
                                                                  return Response(serializer_instace.data,status=status.HTTP_200_OK)
                                                      else:
                                                              return Response(serializer_instace.errors,status=status.HTTP_400_BAD_REQUEST)
                  def delete(self,request,id):
                                                 obj  = get_object_or_404(Employee,id=id)
                                                 self.check_object_permissions(request,obj)
                                                 obj.delete()
                                                 return Response({"message":"deleted sucessfully"},status=status.HTTP_200_OK)
                          
                                                      