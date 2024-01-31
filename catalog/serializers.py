from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Artist, Album, Song, Genre

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ArtistSerializer(serializers.ModelSerializer):
    """
    Automatically sets a pk field (ex: id: 1)
    """
    class Meta:
        model = Artist
        fields = '__all__'    
        read_only_fields = ['last_modified','created']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'