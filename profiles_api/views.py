from rest_framework.views import APIView
from rest_framework.response import Response # when calling the APIVIew it will return you the standard object
from rest_framework import status # returns HTTP status code with the APIs called
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions



#APIView class
# It allows us to define application logic for our endpoint
# basically assigning a URL(endpoint) to this view & then framework calls appropriate functions to get databases
# from HTTP requests
class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer


    #aading an HTTP funtion to an APIVIew
    def get(self, response, format=None):
        """Returns a list of APIVIew features"""
        an_apiview = [
        'Uses HTTP methods as functions (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manuallt to URLs'
        ]

        return Response({'message':"Hello!", 'an_apiview':an_apiview})

    # Adding post functionality to our API view
    def post(self, request):
        """Creating a hello message with our name"""

        #storing in a varibale
        serializer = self.serializer_class(data= request.data) #built-in function which requests the data

        #validating the datab
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    # it updates the entire object
    def put(self, request, pk=None): # pk - primary key - to take the ID of the object
        """Handle updating an object"""
        return Response({"Method":"PUT"})

    # handle the partail update
    def patch(self, request, pk=None):
        """handle the parital update of the object, used for updating fields of the object"""
        return Response({'method':"PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})

# creating a viewset

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    # Adding the serializer class, we can use the same serializers
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """List of features provided by viewset"""

        a_viewset = [
        'uses actions (list, create, retriev, partial_update, update, destroy)',
        'Autoatically maps to URLs using routers',
        'Provides more functionality with less code'
        ]

        return Response({'Message':"Hello", 'a_viewset':a_viewset})

    def create(self, request):
        """Creates a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle retrieval of object on ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle upadting the object based on ID"""
        return Response({'http_method':"PUT"})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object"""
        return Response({'http_method':"PATCH"})

    def destroy(self, request, pk=None):
        """Handles deletion of an object"""
        return Response({'http_method':"DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating & updating porfiles"""

    #creating a serializer class to manage all the operations
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    Authentication_classes = (TokenAuthentication,) # it is a type of authentication we are going to use
    permission_classes = (permissions.UpdateOwnProfile,)
