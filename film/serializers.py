from rest_framework import serializers
from film.models import Movies
from music.models import Song
from review.models import Reviews
from music.serializers import SongSerializers
from review.serializers import ReviewSerializers
class MoviesSerializer(serializers.ModelSerializer):

    greetings=serializers.SerializerMethodField(read_only=True)

    songs_count=serializers.SerializerMethodField(read_only=True)

    songs=serializers.SerializerMethodField(read_only=True)

    review=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Movies
        fields='__all__'
        read_only_fields=['id','created_at','updated_at','end_time','created_by']

    def get_greetings(self,obj):
        return "good morning"

    def get_songs_count(self,obj):
        return Song.objects.filter(movies=obj).count()

    def get_songs(self,obj):
        qs=Song.objects.filter(movies=obj)
        instance=SongSerializers(qs,many=True)
        return instance.data
    
    def get_review(self,obj):
        qs=Reviews.objects.filter(movie=obj)
        instance=ReviewSerializers(qs,many=True)
        return instance.data
