from rest_framework.views import APIView
from rest_framework.response import Response # when calling the APIVIew it will return you the standard object


#APIView class
# It allows us to define application logic for our endpoint
# basically assigning a URL(endpoint) to this view & then framework calls appropriate functions to get databases
# from HTTP requests
class HelloAPIView(APIView):
    """Test API View"""

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
