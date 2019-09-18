from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from . import models
from . import permissions


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


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handles creating, updating and deleting profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    #Here we add the permissions created any
    #We create these as tuples, so they are immutable. also to add multiple
    #Authentications or permissions or filters for searching
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    #search with which fields
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """ Checks email and password and returns an auth token """

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """ Use ObtainAuthToken APIView to validate and create authtoken """

        return ObtainAuthToken().post(request)
