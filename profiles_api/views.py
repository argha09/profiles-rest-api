from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    ''' Test API View '''
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        ''' Returns a list of APIView features '''
        an_apiview = [
            'Arindam Saha',
            'Anirban Mukherjee',
            'Argha Saha',
        ]

        return Response({'message': 'Hello!', 'ap_apiview': an_apiview})
    
    def post(self, request):
        ''' Create a Hello Message with name '''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def put(self, request, pk=None):
        ''' Handle updating an object '''
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        ''' Handle a partial update of an object '''
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        ''' Delete an object '''
        return Response({'method': 'DELETE'})
    

class HelloViewSet(viewsets.ViewSet):
    ''' Test API ViewSet '''
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        ''' Return a Hello Message '''
        an_apiview = [
            'Arindam Saha',
            'Anirban Mukherjee',
            'Argha Saha',
        ]

        return Response({'message': 'Hello!', 'ap_apiview': an_apiview})
    
    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    ''' Handle Creating and Updating Profiles '''
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    ''' Handle creating user authentication token '''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    ''' Handle Create, Read and Update profile feed items '''
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    # permission_classes = (
    #     permissions.UpdateOwnStatus,
    #     IsAuthenticatedOrReadOnly
    # )
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        ''' Set the uer profile to the logged in user '''
        serializer.save(user_profile=self.request.user)