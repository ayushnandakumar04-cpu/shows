from rest_framework import serializers
from film.models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields='__all__'
        read_only_fields=['id','created_at','updated_at','end_time','created_by']