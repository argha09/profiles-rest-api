from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    ''' Test API View '''

    def get(self, request, format=None):
        ''' Returns a list of APIView features '''
        an_apiview = [
            'Arindam Saha',
            'Anirban Mukherjee',
            'Argha Saha',
        ]

        return Response({'message': 'Hello!', 'ap_apiview': an_apiview})
