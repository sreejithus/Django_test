from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Regsiter(APIView):
               def post(self,request):
                            serializer_instance  = UserSerializer(data= request.data)
                            if serializer_instance.is_valid():
                                       serializer_instance.save()
                                       return Response(serializer_instance.data,status=status.HTTP_200_OK)
                            else:
                                      return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class Logout(APIView):
                   permission_classes = [IsAuthenticated]
                   def get(self,request):
                                  self.request.user.auth_token.delete()
                                  return Response({"message":"Logout sucessfull"},status=status.HTTP_200_OK)
                                                                      