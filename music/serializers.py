from rest_framework import serializers
from music.models import Song

class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields='__all__'
        read_only_fields=['id','created_at','updated_at','created_by','movies']