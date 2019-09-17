from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status, viewsets


class HelloApiView(APIView):
    """ Test API View """

    serializer_class = serializers.HelloSerializer
    #format states the suffix options : 'html','json','csv' etc
    def get(self, request, format=None):
        """ Returns a list of APIView features """

        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, delete)',
        'It is similar to a traditional Django view',
        'Gives you the most control over your logic',
        'Is mapped manually to URLs'
        ]
        #Response is a dictionary that is returned in json format
        return Response({'message': 'Hello!','an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with the name being passed """
        #Create an object : request contains all the information for post
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            #Extract the data we need
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            #pass it in response that will create it to json
            return Response({'message': message})
        else:
            return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #pk stands for Primary Key: here its auto-incremented 'id'
    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes and object."""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API viewsets """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return Hello Message """
        a_viewset = [
            'Uses actions list, create, retrieve, update, partial_update',
            'a viewset automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message':'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """ Create a new hello message """
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializers.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Handles getting an object by its ID """

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """ Handles updating an object """

        return Response({'http_method':'UPDATE'})

    def update_partial(self, request, pk=None):
        """ Handles partial updating an object """

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """ Handles deleting an object """

        return Response({'http_method':'DELETE'})
