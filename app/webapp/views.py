from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer, nameSerializer


class employeeList(APIView):

    def get(self,request):
        employeesData = employees.objects.all()
        serializerEmp = employeesSerializer(employeesData, many=True)
        return Response(serializerEmp.data)

    def post(self):
        pass


class nameMessage(APIView):
    def get(self, request, format=None):
        an_apiview=[
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'gives you the most control over your logic',
            'It is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request):
        """ post name to api view """
        serializerMess = nameSerializer(data=request.data)

        if serializerMess.is_valid():
            firstname = serializerMess.data.get('name')
            message = 'Hello {0}'.format(firstname)
            return Response({'message': message})
        else:
            return Response(
            serializerMess.errors, status=status.HTTP_400_BAD_REQUEST)
