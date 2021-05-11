from rest_framework.views import APIView
from rest_framework.response import Response # when calling the APIVIew it will return you the standard object
from rest_framework import status # returns HTTP status code with the APIs called

from profiles_api import serializers


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
