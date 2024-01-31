from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from catalog.serializers import UserSerializer, ArtistSerializer, AlbumSerializer, SongSerializer, GenreSerializer
from .models import Artist, Album, Song, Genre


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    

class ArtistViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        return Artist.objects.all()

class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        return Album.objects.all()
    
class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        return Song.objects.all()

class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        return Genre.objects.all()    